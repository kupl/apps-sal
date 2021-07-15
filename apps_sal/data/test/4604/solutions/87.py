import sys
from collections import deque
p=10**9+7

def main(n,a):
  h=n//2
  g=n%2
  a.sort()
  c=[2*(x//2)+g+1 for x in range(n-g)]
  if g==1:
    c.insert(0,0)
  if a!=c:
      return 0
  return 2**(h%(p-1)) % p

def __starting_point():
  n=int(input())
  a=list(map(int,sys.stdin.readline().strip().split()))
  print((main(n,a)))

__starting_point()
