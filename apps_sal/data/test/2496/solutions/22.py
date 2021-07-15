from functools import reduce
from math import gcd

def sieve(L,R):
    if L<2:L=2
    flag=[0]*(2*R)
    for i in range(2, int(R**.5)+5):
        if flag[i] == 1:continue
        for j in range(i*2,R+i, i):
            if flag[j] == 1:continue
            if j % i == 0:
                flag[j] = 1
    
    return [i for i in range(L,R+1) if flag[i] == 0]
  
N=int(input())
*A,=map(int,input().split())

if N == 2:
  if gcd(A[0],A[1])==1:
    print('pairwise coprime')
  else:
    print('not coprime')
  return

primes = sieve(2,10**6+5)
num = [0]*(2*10**6+10)
for i in range(N):
  num[A[i]] += 1

flag=0
for p in primes:
  count=0
  for d in range(p,10**6+p+5,p):
    count += num[d]
  if count > 1:
    flag=1
    break
  
if flag==0:
  print('pairwise coprime')
elif reduce(gcd,A)==1:
  print('setwise coprime')
else:
  print('not coprime')
