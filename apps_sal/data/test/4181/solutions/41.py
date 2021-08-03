N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = 0
ans = 0
for i in range(N):
    cnt = min(a[i], b[i] + m)
    ans += cnt
    m = min(b[i] + m - cnt, b[i])
ans += min(a[N], m)
print(ans)
