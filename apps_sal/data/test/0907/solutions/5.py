# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353
# INF = 100_000_000

# from heapq import heappush, heappop
# from collections import defaultdict
# from math import sqrt

t = 1  # int(input())

for test in range(t):
    # n = int(input())
    ans = "NO"
    n, m = (((list(map(int, input().split())))))
    arr = []
    for i in range(m):
        a, b = (((list(map(int, input().split())))))
        tmp = [a, b]
        arr.append(tmp)

    x = arr[0][0]
    y = [i for i in range(n + 1)]
    y = set(y)
    for pair in arr:
        if x not in pair:
            y = y.intersection(set(pair))
    if len(y) > 0:
        ans = "YES"

    x = arr[0][1]
    y = [i for i in range(n + 1)]
    y = set(y)
    for pair in arr:
        if x not in pair:
            y = y.intersection(set(pair))
    if len(y) > 0:
        ans = "YES"

    print(ans)
