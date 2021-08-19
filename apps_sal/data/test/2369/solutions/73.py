N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7
comb = [0] * (N + 1)
comb[K - 1] = 1
for i in range(K - 1, N):
    comb[i + 1] = comb[i] * (i + 1) * pow(i - K + 2, -1, mod) % mod
# print(comb)
A.sort()
# mi = sum(a*comb[i]%mod for a, i in zip(reversed(A[:N-K+1]), range(K-1, N)))
# ma = sum(a*comb[i]%mod for a, i in zip((A[K-1:]), range(K-1, N)))
ans = sum((a - b) * comb[i] % mod for b, a, i in zip(reversed(A[:N - K + 1]), A[K - 1:], range(K - 1, N)))
# print(mi%mod, ma%mod)
print(ans % mod)
