n,m=map(int,input().split())
x=[*map(int,input().split())]
have=[False]*10
for i in map(int,input().split()):
  have[i]=True
for i in x:
  if have[i]:
    print(i,end=' ')
