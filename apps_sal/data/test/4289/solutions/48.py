n=int(input())
t,a=map(int,input().split())
l=list(map(int,input().split()))

num=10**5
ans=0

for i,j in enumerate(l):
  tem=abs(a-(t-j*0.006))
  num=min(num,tem)
  if num==tem:
    ans=i+1
    
print(ans)
