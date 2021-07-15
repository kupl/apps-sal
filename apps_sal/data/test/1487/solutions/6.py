S=input()
T=input()
P=''
c=0
A=[0]*len(S)
for i in range(len(S)):
    if S[i]!=T[i]:
        c=c+1
        A[i]=1
if c%2==0:
    for i in range(len(S)):
        if A[i]==1:
            c=c-1
            if c%2==0:
                P=P+T[i]
            else:
                P=P+S[i]
        else:
            P=P+S[i]
    print(P)
else:
    print('impossible')
