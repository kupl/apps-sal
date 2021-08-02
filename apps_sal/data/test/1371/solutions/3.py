from scipy.special import comb
S = int(input())
ans = 0
mod = 10**9 + 7
for i in range(3, S + 1, 3):
    ans = (ans + comb(S - 2 * (i // 3) - 1, i // 3 - 1, exact=True)) % mod
print(ans)
