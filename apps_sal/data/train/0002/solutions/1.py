for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  c=list(map(int,input().split()))
  p=a
  for i in range(n):
    if p[i]==p[(i+1)%n]:
      if p[i]!=b[i] and p[(i-1)%n]!=b[i]:p[i]=b[i]
      else:p[i]=c[i]
  print(*p)
