(N, K) = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in lst:
    if i >= K:
        ans += 1
print(ans)
