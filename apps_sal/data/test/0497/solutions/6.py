n=int(input())
l1=list(map(int,input().split()))
x=0
y=n-1
a=0
b=n-1
while l1[x]==l1[y] and l1[a]==l1[b]:
    y-=1
    a+=1
print(y-x)
