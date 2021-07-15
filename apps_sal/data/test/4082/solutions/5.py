import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

ANS=[0]*n
count=1
ANS[0]=1

ANS2=[0]*n
ucount=0

for i in range(1,n):
    if A[i]>A[i-1]:
        count+=1
        ANS[i]=count

        if ucount>0:
            ucount+=1
            ANS2[i]=ucount
    else:
        count=1
        ANS[i]=count
        ucount=0

    if i>=2 and A[i-2]<A[i]:
        ucount=max(ucount,ANS[i-2]+1)
        ANS2[i]=ucount

print(max((max(ANS)),max(ANS2)))
    

