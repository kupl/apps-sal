n = int(input())
a = list(map(int,input().split()))
b = [0,0] 
for p in range(2):
  s = 0
  for i in range(n):
    t = s+a[i]
    if (i+p)%2 == 0:
      if t<=0:
        b[p] += 1-t
        s = 1
      else:
        s = t
    else:
      if t>=0:
        b[p] += 1+t
        s = -1
      else:
        s = t
print(min(b))
