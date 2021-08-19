import sys
import collections as cc
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
ar = [list(input().strip()) for i in range(n)]
q = cc.deque()
q.append([0, 0])
while q:
    (x, y) = q.pop()
    if x + 1 < n and ar[x + 1][y] == '.':
        ar[x + 1][y] = 1
        q.append([x + 1, y])
    if y + 1 < m and ar[x][y + 1] == '.':
        ar[x][y + 1] = 1
        q.append([x, y + 1])
q = cc.deque()
q.append([n - 1, m - 1])
while q:
    (x, y) = q.pop()
    if x - 1 >= 0 and ar[x - 1][y] == 1:
        ar[x - 1][y] = 0
        q.append([x - 1, y])
    if y - 1 >= 0 and ar[x][y - 1] == 1:
        ar[x][y - 1] = 0
        q.append([x, y - 1])
if ar[n - 1][m - 1] != 1:
    print(0)
else:
    ans = [0] * (n + m + 10)
    for i in range(n):
        for j in range(m):
            if ar[i][j] == 0:
                ans[i + j] += 1
    if 1 in ans:
        print(1)
    else:
        print(2)
