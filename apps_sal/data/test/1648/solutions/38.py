import math


def comb(n, r, mod):
    return math.factorial(n + r - 1) // (math.factorial(n - 1) * math.factorial(r)) % mod


(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
red = n - k
for i in range(k):
    ans = 0
    redmod = red - i
    if redmod < 0:
        print(0)
        continue
    redplace = 2 + i
    bluemod = k - (i + 1)
    if i == 0:
        bluemod = 0
    blueplace = i + 1
    ans += comb(redplace, redmod, mod) * comb(blueplace, bluemod, mod)
    print(ans % mod)
