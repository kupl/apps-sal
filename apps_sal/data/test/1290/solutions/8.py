from sys import stdin, stdout
from random import randrange
sze = 10 ** 3 + 10
(n, m) = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))
cnt = [0 for i in range(sze)]
INF = float('inf')
ans = 0
for v in values:
    cnt[v] += 1
    mn = INF
    for i in range(1, n + 1):
        mn = min(mn, cnt[i])
    ans += mn
    for i in range(1, n + 1):
        cnt[i] -= mn
stdout.write(str(ans))
