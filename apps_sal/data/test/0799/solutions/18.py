n = int(input())
v = list(map(int, input().split()))
k = max(v)
ans = 0
for i in range(n):
    ans += k - v[i]
print(ans)
