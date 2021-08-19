(N, K) = list(map(int, input().split()))
l = sorted(map(int, input().split()), reverse=True)
ans = 0
for i in range(K):
    ans += l[i]
print(ans)
