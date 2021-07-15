N, K = map(int,input().split())
i = list(map(int,input().split()))

ans = 0
for hi in i:
    if hi >= K:
        ans += 1
print(ans)
