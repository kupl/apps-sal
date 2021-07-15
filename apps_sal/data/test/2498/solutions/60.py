import sys
N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
a = []
for i in A:
  i = i//2
  a.append(i)
def gcd(p,q):
  p,q = max(p,q),min(p,q)
  while q!=0:
    p,q = q,p%q
  return p
def lcm(p,q):
  return(p*q//gcd(p,q))
def aaa(i):
  count = 0
  while i%2==0:
    i = i//2
    count+=1
  return count
max_num = a[0]
aa = aaa(a[0])
for i in a:
  max_num = lcm(i,max_num)
  if aa != aaa(i):
    print((0))
    return
print((((M//max_num)+1)//2))

