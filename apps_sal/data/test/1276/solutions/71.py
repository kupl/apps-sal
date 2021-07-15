'''
Created on 2020/09/07

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  S=pin()[:-1]
  r=0
  g=0
  b=0
  cnt=0
  for i in range(N):
    if S[i]=="R":
      r+=1
    elif S[i]=="G":
      g+=1
    elif S[i]=="B":
      b+=1
    for j in range(i+1,N):
      k=2*j-i
      if k>=N:
        continue 
      if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
        cnt+=1
  print(r*g*b-cnt)
  return 
main()
