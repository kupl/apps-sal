from math import gcd
n, k = list(map(int, input().split()))
ans = 1
for e in input().split():
  e = int(e)
  ans = ans // gcd(ans, e) * e % k
print('No' if ans else 'Yes')


