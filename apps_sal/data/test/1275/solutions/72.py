N, K = list(map(int, input().split()))

ans = 0
for ac in range(1 - N, N):
    db = ac - K
    if db < 1 - N or N - 1 < db:
        continue
    ans += (N - abs(ac)) * (N - abs(db))
print(ans)

