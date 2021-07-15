n,v = map(int, input().split())
ans = min(v, n-1)
for i in range(n - v - 1):
    ans += i+2
print(ans)
