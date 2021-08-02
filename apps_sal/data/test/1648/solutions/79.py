import math


def comb(n, r, mod):
    return math.factorial(n + r - 1) // (math.factorial(n - 1) * math.factorial(r)) % mod


n, k = map(int, input().split())
mod = 10**9 + 7
red = n - k

for i in range(k):
    if red - i < 0:
        print(0)
        continue
    ans = comb(2 + i, red - i, mod) * comb(i + 1, k - i - 1, mod)
    print(ans % mod)
