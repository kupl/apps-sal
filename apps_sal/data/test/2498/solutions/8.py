from math import gcd, ceil
N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [a//2 for a in A]
B = 1

for a in A:
  B*=a//gcd(B,a)
  
for a in A:
  if B//a%2==0:
    print(0)
    return

print(ceil((M//B)/2))
