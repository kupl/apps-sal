'''
Created on 2020/08/28

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,M=list(map(int,pin().split()))
  X=list(map(int,pin().split()))
  if N>=M:
    print((0))
    return
  X.sort()
  d=[]
  for i in range(M-1):
    d.append(abs(X[i]-X[i+1]))
  d.sort()
  print((sum(d[:M-N])))
  return 
main()
#解説AC

