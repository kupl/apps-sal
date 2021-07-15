N=int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort(reverse=True)
Arev=sorted(A, reverse=True)
Brev=sorted(B)
atai=0
s=0
for i in range(len(A)):
    if A[i]==B[i]:
        atai=A[i]
        s+=1
C=[]
for i in range(len(A)):
    C.append(A[i]-B[i])
if s>0:
    hajime=C.index(0)
if s==0:
    print("Yes")
    print(*B)
else:
    Acount=A.count(atai)
    Bcount=B.count(atai)
    if N-Acount<Bcount:
        print("No")
    else:
        afirst=A.index(atai)
        alast=N-1-Arev.index(atai)
        bfirst=B.index(atai)
        blast=N-1-Brev.index(atai)
        t=min(afirst,bfirst)
        if t>=s:
            for i in range(0,s):
                B[hajime+i]=B[i]
                B[i]=atai
        else:
            for i in range(0,t):
                B[hajime+i]=B[i]
                B[i]=atai
            ss=s-t
            for i in range(0,ss):
                B[hajime+t+i]=B[-i-1]
                B[-i-1]=atai
        print("Yes")
        print(*B)
