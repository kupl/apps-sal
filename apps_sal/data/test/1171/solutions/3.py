import heapq
import itertools


def main():
    n, k = list(map(int, input().split()))
    v = [int(i) for i in input().split()]
    # k回Vの両端から取り出したり詰めたりして持ってるものの価値の最大化をする
    v_1 = v[::-1]
    # 左から取る回数をA、右から取る回数をBとしたとき、価値が負の宝石を捨てる操作は（k-(A+B)）回できる
    # これを利用して全探索
    res = 0
    for i in range(k + 1):
        j = 0
        while(i + j <= min(n, k)):

            q = []
            tmp = 0
            if(i > 0):
                for l in range(i):
                    if(v[l] < 0):
                        heapq.heappush(q, v[l])
                    tmp += v[l]
            if(j > 0):
                for l in range(j):
                    if(v_1[l] < 0):
                        heapq.heappush(q, v_1[l])
                    tmp += v_1[l]
            for l in range(k - (i + j)):
                if(len(q) > 0):
                    z = heapq.heappop(q)
                    tmp -= z
            j += 1
            res = max(res, tmp)

    print(res)


def __starting_point():
    main()


__starting_point()
