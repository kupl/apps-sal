import bisect
N, K = list(map(int,input().split()))
a = list(map(int,input().split()))
S = [0]*N
S[0] = a[0]
for k in range(1,N):
    S[k] = S[k-1] + a[k]
S = [0] + S
ans = 0
for k in range(N+1):
    if S[k] >= K:
        ans += bisect.bisect_right(S,S[k]-K)
print(ans)

