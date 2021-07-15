n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))
ans=0
res=float('inf')
for i in range(n):
  if abs(t-h[i]*float(0.006)-a)<res:
    res=abs(t-h[i]*float(0.006)-a)
    ans=i+1
print(ans)
