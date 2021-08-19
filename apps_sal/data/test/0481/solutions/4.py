from math import ceil, sqrt
(n, x) = map(int, input().split())
cnt = 0
s = set()
for i in range(1, ceil(sqrt(x)) + 1):
    if x % i == 0 and i <= n and (x / i <= n):
        s.add(i)
        s.add(x // i)
print(len(s))
