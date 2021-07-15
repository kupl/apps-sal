from math import gcd
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=list(set(a))
a=list(map(lambda x: x//2, a))

def lcm(q):
  x = q[0]
  for i in range(1, len(q)):
    x = (x * q[i]) // gcd(x, q[i])
  return x

lcma=lcm(a)
for i in range(len(a)):
  if (lcma//a[i])%2==0:
    print(0)
    return
temp=m//lcma
print(temp//2 if temp%2==0 else temp//2+1)
