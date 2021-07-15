'''
Created on 2020/10/01

@author: harurun
'''
import sys
pin=sys.stdin.readline

def main():
  N=int(pin())
  a=list(map(int,pin().split()))
  d=[0]*(10**5)
  for i in a:
    d[i]+=1
  ans=0
  for i in range(10**5-2):
    ans=max(ans,d[i]+d[i+1]+d[i+2])
  print(ans)
  return 
main()
