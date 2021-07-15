from math import gcd
from sys import stdin
pin=stdin.readline
def lcm(a,b):
  return a*b//gcd(a,b)

def main():
  N=int(pin())
  k=2
  for i in range(3,N+1):
    k=lcm(k,i)
  print(k+1)
  return

main()
