from math import ceil, sqrt, factorial, gcd
from bisect import bisect_left
from collections import deque
from sys import stdin


def input():
    return stdin.readline().strip()


(n, m) = list(map(int, input().split()))
s = input()
x = []
y = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    x.append(a)
    y.append(b)


def beauty(n, m, s, x, y):
    l = list(s)
    degree = [0 for i in range(n)]
    graph = {i: [] for i in range(n)}
    for i in range(m):
        (a, b) = (x[i], y[i])
        a -= 1
        b -= 1
        graph[a].append(b)
        degree[b] += 1
    q = deque()
    for i in range(n):
        if degree[i] == 0:
            q.append(i)
    count = 0
    ans = 0
    dp = [[0 for i in range(26)] for i in range(n)]
    while count < n and q:
        x = q.popleft()
        count += 1
        dp[x][ord(l[x]) - 97] += 1
        for i in graph[x]:
            for j in range(26):
                dp[i][j] = max(dp[i][j], dp[x][j])
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
    if count != n:
        print(-1)
    else:
        ans = 0
        for i in range(n):
            ans = max(ans, max(dp[i]))
        print(ans)


beauty(n, m, s, x, y)
