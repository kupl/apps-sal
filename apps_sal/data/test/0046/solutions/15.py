import math

n, m = list(map(int, input().split()))

ndiv = math.floor(n / 5)
nmod = n % 5

mdiv = math.floor(m / 5)
mmod = m % 5

mods = 0
if nmod + mmod >= 5:
    mods = nmod + mmod - 4

ans = (ndiv * mdiv * 5) + nmod * mdiv + mmod * ndiv + mods
print(ans)
