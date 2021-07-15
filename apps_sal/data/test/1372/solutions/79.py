h,n = map(int, input().split())
ab = []
amax = 10**5
for _ in range(n):
  ab.append(tuple(map(int,input().split())))
amax = max(a for a,b in ab)
p = [0]*(h+amax+1)
for i in range(1,h+amax):
  p[i] = min(p[i-a]+b for a,b in ab)
print(p[h])
