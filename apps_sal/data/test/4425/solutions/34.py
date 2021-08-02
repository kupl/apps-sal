N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    if i >= K:
        ans += 1 / N
    else:
        x = 0
        while i < K:
            i *= 2
            x += 1
        ans += (1 / N) * (1 / 2)**x
print(ans)
