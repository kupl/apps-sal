import math
import collections
def prime_diviation(n):
    factors = []
    i = 2
    while i <= math.floor(math.sqrt(n)):
        if n%i == 0:
            factors.append(int(i))
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

N = int(input())
if N == 1:
  print(0)
  return
#pr:素因数分解 prs:集合にしたやつ prcnt:counter
pr = prime_diviation(N)
prs = set(pr)
prcnt = collections.Counter(pr)
#print(pr, prs, prcnt)
ans = 0

for a in prs:
  i = 1
  cnt = 2*prcnt[a]
  #2*prcnt >= n(n+1)となる最大のnを探すのが楽そう
#  print(cnt)
  while cnt >= i*(i+1):
    i += 1
  ans += i - 1 
  
print(ans)  
