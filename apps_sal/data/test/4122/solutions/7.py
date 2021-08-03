# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353
INF = 100_000_000
# from heapq import heappush, heappop
# from collections import defaultdict
t = 1  # int(input())
# from math import sqrt


for test in range(t):
    # n = int(input())
    H, n = (list(map(int, input().split())))
    # a = []
    # for i in range(n):
    # l = input()
    # r = input()
    d = (list((list(map(int, input().split())))))
    pre = [0 for i in range(n + 1)]

    minVal = pre[0]
    minInd = 0
    for i in range(n):
        pre[i + 1] = pre[i] + d[i]
        if pre[i + 1] < minVal:
            minInd = i + 1
            minVal = pre[i + 1]

    h = H
    ans = 0
    for i in d:
        ans += 1
        h += i
        if h <= 0:
            print(ans)
            return
    if pre[-1] >= 0:
        print(-1)
    else:
        h = H
        h += minVal
        tmp = (h - pre[-1] - 1) // (-pre[-1])
        # print(tmp, minVal, pre[-1])
        ans = tmp * (n)
        h = H
        h += pre[-1] * tmp
        for i in d:
            ans += 1
            h += i
            if h <= 0:
                print(ans)
                break
