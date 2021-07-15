N=int(input())
a=list(map(int,input().split()))
y=sum(a)
x=0
B=[]
for i in range(N-1):
    x+=a[i]
    y-=a[i]
    B.append(abs(x-y))

print(min(B))
