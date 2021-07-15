'''
Created on 2020/08/27

@author: harurun
'''
def main():
  import math
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  a,b,x=map(int,pin().split())
  if 2*x>a*a*b:
    print(math.degrees(math.atan((2*b*a*a-2*x)/(a*a*a))))
  else:
    print(math.degrees(math.atan(a*b*b/(2*x))))
  return 

main()
