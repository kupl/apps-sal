mod = 10**9 + 7
K = int(input())
S = input()
n = len(S)
tmp = pow(26, K, mod)
waru = pow(26, -1, mod)
ans = tmp
for i in range(1, K+1):
    tmp = (tmp * 25 * waru)%mod
    tmp = (tmp * (i + n -1) * pow(i, -1, mod))%mod
    ans = (ans+tmp)%mod
print(ans%mod)
