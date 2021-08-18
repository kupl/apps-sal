import heapq
import itertools


def main():
    n, k = list(map(int, input().split()))
    v = [int(i) for i in input().split()]
    v_1 = v[::-1]
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
