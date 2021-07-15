'''
Created on 2020/10/01

@author: harurun
'''
import sys
pin=sys.stdin.readline

def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)

def lcm(a,b):
  return a*b//gcd(a,b)

def main():
  N=int(pin())
  a=list(map(int,pin().split()))
  s=a[0]
  for i in range(N-1):
    s=lcm(a[i+1],s)
  ans=0
  for i in a:
    ans+=(s-1)%i
  print(ans)
  return
main()
