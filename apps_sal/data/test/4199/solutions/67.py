(N, K) = map(int, input().split())
h = list(map(int, input().split()))
ans = 0
for h_ in h:
    if h_ >= K:
        ans += 1
print(ans)
