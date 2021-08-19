K = int(input())
S = input()
s = len(S)
mod = int(1000000000.0 + 7)
n = pow(26, K, mod)
ans = n
for i in range(K):
    n = n * 25 * (s + i) * pow(26 * (i + 1), -1, mod) % mod
    ans = (ans + n) % mod
print(ans)
