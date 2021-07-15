n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(n*2):
    b.append(0)
for i in range(n):
    if(i+a[i]<=n):
        b[i+a[i]]+=1
    if(i>=a[i]):
        c+=b[i-a[i]]

print(c)
