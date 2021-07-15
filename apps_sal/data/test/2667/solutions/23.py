n=int(input())
l=list(map(int,input().strip().split()))
s=sum(l)
k=0
for i in range(0,len(l)+1):
    k=k+i

if s==k:
    print("YES")
else:
    print("NO")
