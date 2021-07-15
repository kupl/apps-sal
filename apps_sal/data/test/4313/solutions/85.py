n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(n):
  ans += max(v[i]-c[i],0)
print(ans)
