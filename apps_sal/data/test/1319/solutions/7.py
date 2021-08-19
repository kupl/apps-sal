from collections import Counter as C
from operator import __mul__
mod = 10 ** 9 + 7
n = int(input())
m = C(map(int, input().split()))
ans = mul = 1
for elem in m.values():
    mul *= elem + 1
for (a, b) in m.items():
    curr = mul * b // 2
    curr %= mod - 1
    ans *= pow(a, curr, mod)
    ans %= mod
print(ans)
