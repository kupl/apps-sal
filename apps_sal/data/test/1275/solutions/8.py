N, K = map(int, input().split())

cnt = [0] * (2*N+1)

for i in range(0,2*N+1):
    if i > 1 and i < N+2 : cnt[i] = cnt[i-1]+1
    elif i >= N+2: cnt[i] = cnt[i-1]-1
ans = 0


for i in range(K+2,2*N+1):
    if i < 2: continue
    if 2*N >= i-K >= 1:
        ans += cnt[i]*cnt[i-K]
print(ans)
