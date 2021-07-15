import math

def lcm(x, y):
  return (x * y) // math.gcd(x, y)

def kazu(s,e,n):
  if s%n>0:
    s2=s-s%n
    s2+=n
  else:
    s2=s
  e2=e-e%n
  if s<=s2<=e and s<=e2<=e:
    return ((e2-s2+n)//n)
  return 0

a,b,c,d=list(map(int,input().split()))

nc = kazu(a,b,c)
nd = kazu(a,b,d)
ncd = kazu(a,b,lcm(c,d))

ans = b-a+1

ans -= nc
ans -= nd
ans += ncd

print(ans)

