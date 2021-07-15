n,b,d=list(map(int,input().split()))
a=list(map(int,input().split()))
q,k=0,0
for i in range(n):
    if a[i]>b:
        continue
    else:
        k+=a[i]
        if k>d:
            q+=1
            k=0
print(q)

