n,c = map(int,input().split())
a = [(0,0)]
for _ in range(n):
  x,v = map(int,input().split())
  a += [(x,v)]
a += [(0,0)]
max_r, max_l = [0], [0]
s = 0
for i in range(1, n+1):
  s += a[i][1]
  max_r += [max(max_r[i-1], s-a[i][0])]
max_r += [0]
s = 0
for i in range(1, n+1):
  s += a[-i-1][1]
  max_l += [max(max_l[i-1], s-c+a[-i-1][0])]
max_l += [0]
max_l.reverse()
ans = 0
for i in range(1, n+1):
  ans = max(ans, max_r[i], max_l[i], max_r[i]+max_l[i+1]-a[i][0], max_r[i-1]+max_l[i]-c+a[i][0])
print(ans)
