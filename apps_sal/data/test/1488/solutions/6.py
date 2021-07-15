def gcd (n,m):
  if n % m == 0: return m
  return gcd (m, n%m)

n = int (eval(input ()))
a = list (map (int, input().split()))
a.sort()

s = a[0]
sleft = 0
for i in range (1,len(a)):
  sleft += (i*a[i] - s)
  s += a[i]

tot = s + sleft*2
print(tot//gcd(tot,n), n//gcd(tot,n))

