import math
def cmb(n,r):
  return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
n=int(input())
a=list(map(int,input().split()))
a.sort()
ls=[0]
cnt=0
for i in range(1,2**n):
  if a[i]>a[i-1]:
    cnt+=1
  ls.append(cnt)
lmt = []
for i in range(n+1):
  lmt.extend([i]*cmb(n,i))
bias = ls[-1]-lmt[-1]
jdg = 0
ulmt = 0
for i in range(n):
  jdg += ls.count(i)
  ulmt += 2**(n-i-1)
  if jdg > ulmt:
    print("No")
    return
for x,l in zip(ls,lmt):
  if x-l > bias:
    print("No")
    break
else:
  print("Yes")
