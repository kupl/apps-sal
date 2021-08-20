from sys import stdin, stdout
from collections import deque
(n, d) = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))
ans = set()
for i in range(n):
    cur = values[i] - d
    mn = 10 ** 10
    for j in range(n):
        if abs(cur - values[j]) < mn:
            mn = abs(cur - values[j])
    if mn == d:
        ans.add(cur)
    cur = values[i] + d
    mn = 10 ** 10
    for j in range(n):
        if abs(cur - values[j]) < mn:
            mn = abs(cur - values[j])
    if mn == d:
        ans.add(cur)
stdout.write(str(len(ans)))
