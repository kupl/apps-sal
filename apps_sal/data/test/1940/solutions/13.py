(n, k) = map(int, input().split())
l = sorted(map(int, input().split()))
ans = 0
for i in range(n):
    ans += -(-l[i] // k)
print(-(-ans // 2))
