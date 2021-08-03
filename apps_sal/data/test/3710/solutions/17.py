import sys
from math import gcd
input = sys.stdin.readline
n, k = map(int, input().split())
v = list(map(int, input().split()))
lcm = 1
for u in v:
    lcm = lcm * u // gcd(u, lcm)
    lcm = gcd(lcm, k)
print(["No", "Yes"][lcm == k])
