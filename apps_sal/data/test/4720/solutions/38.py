N=int(input())
l=[0]*N
r=[0]*N
sum=0
for i in range(N) :
  l[i],r[i]=map(int,input().split())
  sum+=r[i]-l[i]+1
print(sum)
