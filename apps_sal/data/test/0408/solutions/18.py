import sys

nm=list(map(int,sys.stdin.readline().split()))
n=nm[0]
m=nm[1]
g=0
while n>0 and m>0 and n+m>2:
  if n>m:
    g=g+1
    n=n-2
    m=m-1
  else:
    g=g+1
    m=m-2
    n=n-1

print(g)
