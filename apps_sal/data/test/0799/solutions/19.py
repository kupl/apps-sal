n = int(input())
a = list(map(int , input().split()))
maxim = max(a)
ans = 0
for i in range(n):
    ans += a[i] - maxim
print(-ans)
