import sys
def make_divisors(n):
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]
N,M=map(int,input().split())
c=M//N
L=make_divisors(M)
L=list(reversed(L))
for i in range(len(L)):
  if L[i]<=c:
    print(L[i])
    return
