import sys
sys.setrecursionlimit(2000)
def joken(a,n):
  if n==1:
    return 0
  elif a%n==0 and a//n>=n:
    return joken(a//n,n)
  elif a%n==1:
    return 1
  elif a%n==0 and a//n==1:
    return 1
  else:
    return 0
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
N=int(input())
c=len(make_divisors(N-1))
d=make_divisors(N)
a=0
for i in range(len(d)):
  a+=joken(N,d[i])
print(a+c-1)
