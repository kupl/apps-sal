n=int(input())
k=int(input())
x=list(map(int,input().split()))
ans=0
for  i in range(n):
  m=min(abs(x[i]),abs(k-x[i]))
  ans+=m

print(ans*2)
