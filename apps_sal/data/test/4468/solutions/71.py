n, t = map(int, input().split())
a = list(map(int, input().split())) + [10**10]

ans = 0
for i in range(n):
  ans += min(a[i+1] - a[i], t)

print(ans)
