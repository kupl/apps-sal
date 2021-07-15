n = int(input())
a = sorted(map(int, input().split()))
p = a[-1]
c = 0
for i in range(n-1):
  if abs(a[i+1]-p/2) < abs(a[i]-p/2):
    c = a[i+1]
  else:
    break
print(p,c)
