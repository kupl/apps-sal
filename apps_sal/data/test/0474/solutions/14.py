n=int(input())
A=list(map(int,input().split()))

M=max(A)
ANS=0
count=0
for a in A:
    if a==M:
        count+=1
        if ANS<count:
            ANS=count
    else:
        count=0
print(ANS)

