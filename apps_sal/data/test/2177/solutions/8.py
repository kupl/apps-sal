n=int(input())
for i in range(n):
  A,B=map(int,input().split())
  l=1;ans=0
  while 10**l-1<=B:
    ans+=1
    l+=1
  print(ans*A)
