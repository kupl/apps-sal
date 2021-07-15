n,k=map(int,input().split())
data=list(map(int,input().split()))
y=sorted(data)
s=0
for i in range(0,k):
    s=s+y[n-1-i]
print(s)
