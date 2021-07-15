n = int(input())
d,x = map(int,input().split())
a = [int(input()) for i in range(n)]
ans = x
for i in range(n):
  j = 0
  while j*a[i]+1 <= d:
    ans += 1
    j += 1
print(ans)
