import sys

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))

if n==1:
    print(0)
    return

A.sort(reverse=True)

NOW=A[0]
ANS=1
i=1
while i<n:
    if A[i]==A[i-1]:
        NOW=max(1,NOW-1)
        ANS+=1
    else:
        if A[i]>=NOW-1:
            ANS+=1
            NOW=max(NOW-1,1)
        else:
            ANS+=max(1,NOW-A[i])
            NOW=A[i]
    i+=1
    #print(i,ANS,NOW)

ANS+=(NOW-1)
print(sum(A)-ANS)

