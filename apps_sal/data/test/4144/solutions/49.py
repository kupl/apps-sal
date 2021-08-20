from scipy.special import perm
N = int(input())
mod = 1000000007
ans = 10 ** N - 9 ** N - 9 ** N + 8 ** N
ans %= mod
print(ans)
