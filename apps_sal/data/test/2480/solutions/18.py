from collections import Counter

N, K = list(map(int, input().split()))
*A, = list(map(int, input().split()))
MOD = 10**9+7
S = [0]*(N+1)
c = Counter()
c[0] = 1
ans = 0

for i in range(N):
    S[i+1] = (S[i]+A[i]-1)%K
    if i+1-K>=0:
        c[S[i+1-K]] -= 1
    ans += c[S[i+1]]
    c[S[i+1]] += 1

print(ans)

