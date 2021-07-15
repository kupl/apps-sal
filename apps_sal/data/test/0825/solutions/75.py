'''
Created on 2020/08/23

@author: harurun
'''
def f(n):
  arr=[]
  temp=n
  for c in range(2,int(-(-n**0.5//1))+1):
    if temp%c==0:
      cnt=0
      while temp%c==0:
        cnt+=1
        temp//=c
      arr.append([c,cnt])
  if temp!=1:
    arr.append([temp,1])
  return arr

def main():
  import math
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  r=f(N)
  ans=0
  for i in r:
    ans+=int((math.sqrt(1+8*i[1])-1)/2)
  print(ans)
  return 
main()
