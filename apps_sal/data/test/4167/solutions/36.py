n,k=list(map(int,input().split()))


kcd=0
kcd_half=0
for i in range(1,n+1):
    if k&1 and i%k==0:
        kcd+=1
    elif not k&1:
        if i%k==0:
            kcd+=1
        if i%k==k//2:
            kcd_half+=1

print((kcd*kcd*kcd+kcd_half*kcd_half*kcd_half))

