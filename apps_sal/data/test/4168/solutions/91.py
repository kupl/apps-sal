n = int(input())
if n == 0:
  print(0)
  return
a = [1]
p = [1]
m = [0]
hi = [1]
lo = [1]
i = 0
while(True):
  if n >= lo[i] and n<= hi[i]:
    break
  i += 1
  a.append(a[i-1]*-2)
  if i%2==0:
    p.append(p[i-1]+a[i])
    m.append(m[i-1])
  else:
    p.append(p[i-1])
    m.append(m[i-1]+a[i])
  hi.append(a[i]+p[i-1])
  lo.append(a[i]+m[i-1])
ans = []
for j in range(i+1)[::-1]:
  if n >= lo[j] and n<= hi[j]:
    ans.append(1)
    n-=a[j]
  else:
    ans.append(0)
print(*ans,sep="")
