import math


def c(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n = int(input())
d = dict()
for _ in range(n):
    s = "".join(sorted([c for c in input()]))
    d[s] = d.get(s, 0) + 1

ans = 0
for v in d.values():
    if v >= 2:
        ans += c(v, 2)
print(ans)
