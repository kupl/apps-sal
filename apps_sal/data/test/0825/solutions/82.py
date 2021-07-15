import collections
import bisect
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
c = collections.Counter(prime_factorize(N))
sums = []
s=1
ans = 0
for v in c.values():
  count = 0
  for i in range(1,v+1):
    if count+i > v:
      break
    else:
      count += i
      ans += 1
print(ans)
