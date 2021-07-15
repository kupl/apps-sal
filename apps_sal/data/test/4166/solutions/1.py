'''
Created on 2020/09/10

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,M=map(int,pin().split())
  if N==3:
    ans=[1,0,0]
    for _ in [0]*M:
      s,c=map(int,pin().split())
      if s==1 and c==0:
        print(-1)
        return 
      if s!=1 and ans[s-1]!=0 and ans[s-1]!=c:
        print(-1)
        return 
      ans[s-1]=c
    a=""
    for i in ans:
      a+=str(i) 
    print(a)
    return 
  elif N==2:
    ans=[1,0]
    for _ in [0]*M:
      s,c=map(int,pin().split())
      if s==1 and c==0:
        print(-1)
        return 
      if s!=1 and ans[s-1]!=0 and ans[s-1]!=c:
        print(-1)
        return 
      ans[s-1]=c
    a=""
    for i in ans:
      a+=str(i)
    print(a)
    return
  else:
    if M==0:
      print(0)
      return
    s,c=map(int,pin().split())
    ans=c 
    
    for j in range(M-1):
      s,c=map(int,pin().split())
      if c!=ans:
        print(-1)
        return 
    print(ans)
    return 
  
main()
