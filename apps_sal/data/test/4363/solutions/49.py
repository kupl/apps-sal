'''
Created on 2020/09/03

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  K,S=map(int,pin().split())
  ans=0
  for x in range(K+1):
    for y in range(K+1):
      if 0<=S-x-y<=K:
        ans+=1
  print(ans)
  return 
main()
