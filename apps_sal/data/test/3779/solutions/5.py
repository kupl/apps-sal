from math import gcd

N, K = map(int, input().split())
A = list(map(int, input().split()))

g = 0
for Ai in A: g = gcd(g, Ai)

s = set()
x = 0
while x not in s:
    s.add(x)
    x = (x + g) % K

print(len(s))
print(*sorted(s))
