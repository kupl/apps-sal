N = int(input())
mod = 998244353
Ans = []
nums = pow(10, N, mod)
nums_inv = pow(nums, mod-2, mod)
inv10 = pow(10, mod-2, mod)
for d in range(1, N):
    ans = 0
    ans += pow(inv10, d, mod) * 9 * nums * 2 % mod
    ans += (N-d-1) * pow(inv10, d+1, mod) * 81 * nums % mod
    Ans.append(ans%mod)
Ans.append(10)
print(" ".join(map(str, Ans)))

