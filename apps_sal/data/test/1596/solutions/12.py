from itertools import groupby
dp0 = [0, 1]
dp1 = [0, 0]
d0, d1 = 1, 0
A = [0, 1]
mod = 10**9 + 7
for i in range(2, 101010):
    d0, d1 = (d0 + d1) % mod, d0
    dp0.append(d0)
    dp1.append(d1)
    A.append(d0 + d1)

S = input()
ans = 1
for c, g in groupby(S):
    if c == "n" or c == "u":
        n = len(list(g))
        ans = ans * A[n] % mod
    elif c == "m" or c == "w":
        ans = 0
print(ans)
