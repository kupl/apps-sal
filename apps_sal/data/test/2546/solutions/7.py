import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


def solve():
    (ls, rs) = ([], [])
    (n, money) = getList()
    sals = []
    for _ in range(n):
        (a, b) = getList()
        sals.append((a, b))
    ans_mx = 10 ** 10
    ans_mn = 0
    while ans_mx - ans_mn > 1:
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
        while heap:
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
    while heap:
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


'\n1\n3 26\n10 12\n1 4\n10 11\n\n1\n1 100\n1 1\n\n1\n3 6\n1 1000\n2 1000\n3 1000\n\n\n1\n9 100\n2 4\n3 5\n8 100\n25 100\n2 39\n1 2\n23 40\n1 20\n2 10\n'
__starting_point()
