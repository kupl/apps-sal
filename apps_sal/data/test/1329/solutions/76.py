def calc(N,p):
  ans = 0
  i = p
  while N>=i:
    ans += N//i
    i *= p
  return ans

def sieve(n):
  is_prime = [True for _ in range(n+1)]
  is_prime[0] = False
  for i in range(2, n+1):
    if is_prime[i-1]:
      j = 2 * i
      while j <= n:
        is_prime[j-1] = False
        j += i
  table = [i for i in range(1, n+1) if is_prime[i-1]]
  return table
  
from itertools import groupby, accumulate, product, permutations, combinations
def check(value,lis):
  ans = 0
  n = len(lis)
  for perm in permutations(value,n):
    for i in range(n):
      if perm[i]<lis[i]:
        break
    else:
      ans += 1
  return ans

def solve():
  N = int(input())
  table = sieve(N)
  v = []
  for p in table:
    v.append(calc(N,p))
  v.sort(reverse=True)
  ans = 0
  ans += check(v,[74])
  ans += check(v,[24,2])
  ans += check(v,[14,4])
  ans += check(v,[4,4,2])//2
  return ans
print(solve())
