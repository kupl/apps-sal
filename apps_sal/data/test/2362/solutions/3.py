"""

created by shuangquan.huang at 1/16/19

"""
import collections
import time
import os
import sys
import bisect
import heapq
N = int(input())
A = [0] + [int(x) for x in input().split()]
G = collections.defaultdict(list)
for i in range(N - 1):
    (x, y) = list(map(int, input().split()))
    G[x].append(y)
    G[y].append(x)


def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


dp = [[] for _ in range(N + 1)]


def dfs(node, parent):
    chd = []
    ans = 0
    for u in G[node]:
        if u != parent:
            ans = max(ans, dfs(u, node))
            for t in dp[u]:
                chd.append(t)
    chd.sort()
    i = 0
    while i < len(chd):
        j = i - 1
        (mx1, mx2) = (0, 0)
        while j + 1 < len(chd) and chd[j + 1][0] == chd[i][0]:
            j += 1
            if chd[j][1] >= mx1:
                (mx2, mx1) = (mx1, chd[j][1])
            elif chd[j][1] > mx2:
                mx2 = chd[j][1]
        if A[node] % chd[i][0] == 0:
            ans = max(ans, mx1 + mx2 + 1)
            dp[node].append((chd[i][0], mx1 + 1))
            while A[node] % chd[i][0] == 0:
                A[node] //= chd[i][0]
        else:
            ans = max(ans, mx1)
        i = j + 1
    i = 2
    while i * i <= A[node]:
        if A[node] % i == 0:
            dp[node].append((i, 1))
            ans = max(ans, 1)
            while A[node] % i == 0:
                A[node] //= i
        i += 1
    if A[node] > 1:
        dp[node].append((A[node], 1))
        ans = max(ans, 1)
    return ans


print(dfs(1, -1))
