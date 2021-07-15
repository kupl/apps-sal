n=int(input())
h=list(map(int,input().split()))

flag=True
for i in range(1,n):
    if h[i-1]>h[i]:
        flag=False
    elif h[i-1]<h[i]:
        h[i]=h[i]-1
print("Yes" if flag else "No")
