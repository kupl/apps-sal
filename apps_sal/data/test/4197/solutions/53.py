n=int(input())
s={i+1:int(x) for i,x in enumerate(input().split())}
s=sorted(s.items(), key=lambda x:x[1])
for i,j in s:
  print(i,end=' ')

