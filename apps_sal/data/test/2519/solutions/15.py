N, K = map(int, input().split())
p = list(map(int, input().split()))


expected = [0] * N
for i in range(N):
    expected[i] = (p[i] + 1) / 2

ans = 0
agg = 0
for i in range(N):
    if i < K:
        agg += expected[i]
    else:
        agg += expected[i]
        agg -= expected[i - K]
    ans = max(ans, agg)
print(ans)
