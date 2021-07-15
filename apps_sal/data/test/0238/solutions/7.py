import copy

n,m,k=list(map(int,input().split()))
A=list(map(int,input().split()))

ANS=0

for i in range(m):
    B=copy.deepcopy(A)
    for j in range(i,n,m):
        B[j]-=k

    NOW=0

    for j in range(i,n):
        if j%m==i:
            NOW=max(NOW+B[j],B[j])
        else:
            NOW+=B[j]

        ANS=max(ANS,NOW)

print(ANS)
        
    

