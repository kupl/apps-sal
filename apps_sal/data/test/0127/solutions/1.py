from sys import stdin, stdout
import math

n, k = map(int, stdin.readline().split())
values = []
ans = 0

for i in range(n):
    a, b = map(int, stdin.readline().split())
    ans += min(a, b)

    if a < b:
        b -= a
        values.append(min(a, b))


values.sort()
for v in values[::-1]:
    if not k:
        break

    ans += v
    k -= 1


stdout.write(str(ans))
