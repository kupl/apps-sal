k,l=list(map(int,input().split()))
for i in range(0,l):
    if k%10==0:
        k=k/10
    else:
        k=k-1
print(int(k))

