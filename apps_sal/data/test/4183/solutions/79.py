#最大公約数
def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

#最小公倍数
def lcm(a,b):
  return a*b//gcd(a,b)

#全ての最小公倍数を求めればいい
n=int(input())
ans=1
for i in range(n):
  ans=lcm(ans,int(input()))
print(ans)

  




