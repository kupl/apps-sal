k, n = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
for i in range(n):
    ans += p[i]
print(ans)
