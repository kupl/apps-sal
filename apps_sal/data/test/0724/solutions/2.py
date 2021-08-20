from sys import stdin, stdout
from random import randrange
(n, d) = map(int, stdin.readline().split())
points = sorted(list(map(int, stdin.readline().split())))
ans = n
for i in range(n):
    for j in range(n - 1, i - 1, -1):
        if points[j] - points[i] <= d:
            ans = min(ans, n - (j - i + 1))
stdout.write(str(ans))
