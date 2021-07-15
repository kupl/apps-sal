n, m = map(int, input().split())
a = list(map(int,input().split()))
x = 0
ans = 0

for i in range(n):
  x += a[i]
  
for i in a:
    if i >= x*1/(4*m):
        ans += 1
if ans >= m:
    print('Yes')
else:
    print('No')
