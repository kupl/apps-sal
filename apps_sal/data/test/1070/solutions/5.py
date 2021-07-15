n,k=map(int,input().split())
a=list(map(int,input().split()))
mx=1
ct=1
for i in range(1,n):
    if a[i]!=a[i-1]:
        ct+=1
    mx=max(mx,ct)
    if a[i]==a[i-1]:
        ct=1
print(mx)        
