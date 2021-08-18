import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def solve():
    ls, rs = [], []
    n, money = getList()
    sals = []
    for _ in range(n):
        a, b = getList()
        sals.append((a, b))

    ans_mx = 10**10
    ans_mn = 0
    while(ans_mx - ans_mn > 1):
        tmp = 0
        heap = []
        mid = (ans_mn + ans_mx) // 2
        for sal in sals:
            if sal[1] < mid:
                tmp += sal[0]
            else:
                heapq.heappush(heap, (-sal[0], -sal[1]))

        if len(heap) < (n + 1) // 2:
            ans_mx = mid
            continue

        high = 0
        tgt = n // 2
        while(heap):
            sal_cur = heapq.heappop(heap)
            if high <= tgt:
                tmp += max(mid, -sal_cur[0])
                high += 1
            else:
                tmp += -sal_cur[0]

        if tmp <= money:
            ans_mn = mid

        else:
            ans_mx = mid

    tmp = 0
    heap = []
    mid = ans_mx
    for sal in sals:
        if sal[1] < mid:
            tmp += sal[0]
        else:
            heapq.heappush(heap, (-sal[0], -sal[1]))

    if len(heap) < (n + 1) // 2:
        print(ans_mn)
        return

    high = 0
    tgt = n // 2
    while (heap):
        sal_cur = heapq.heappop(heap)
        if high <= tgt:
            tmp += max(mid, -sal_cur[0])
            high += 1
        else:
            tmp += -sal_cur[0]
    if tmp <= money:
        print(mid)
        return

    else:
        print(ans_mn)
        return


def main():
    t = getN()
    for times in range(t):
        solve()


def __starting_point():
    main()


"""
1
3 26
10 12
1 4
10 11

1
1 100
1 1

1
3 6
1 1000
2 1000
3 1000


1
9 100
2 4
3 5
8 100
25 100
2 39
1 2
23 40
1 20
2 10
"""
__starting_point()
