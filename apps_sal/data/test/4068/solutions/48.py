n,m = map(int,input().split())
l = set([int(input()) for i in range(m)])
c = [0]*(n+1)
c[0]=1
c[1]=1
if 1 in l:
  c[1]=0
for i in range(2,n+1):  
  if i in l:
    c[i] = 0 
  else:
    c[i] = (c[i-1]+c[i-2])%1000000007
print(c[n])
