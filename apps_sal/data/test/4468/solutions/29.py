n, t = map(int, input().split())
L = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    ans += min(t, L[i+1] - L[i])
ans += t
print(ans)
