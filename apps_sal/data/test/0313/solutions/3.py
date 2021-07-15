n=int(input())
l=list(map(int,input().split()))
for i in range(2,n):
    if l[i]==1 and l[i-1]==0 and l[i-2]==1: l[i-1]=1
print(l.count(1))
