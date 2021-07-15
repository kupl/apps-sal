a,b=map(int,input().split())
N=b-a
c=0

for i in range(N+1):
  c=c+i

print(c-b)
