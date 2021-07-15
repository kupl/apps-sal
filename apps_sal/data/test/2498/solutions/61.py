import math
def lcm(a,b):
  return (a*b)//math.gcd(a,b)
def co(num):
  return format(num, 'b')[::-1].find('1')
N,M=map(int,input().split())
L=list(map(int,input().split()))
L2=[co(i) for i in L]
if len(set(L2))!=1:
  print(0)
  return
L=[i//2 for i in L]
s=L[0]
for i in range(N):
  s=lcm(s,L[i])
c=M//s
print((c+1)//2)
