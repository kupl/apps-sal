import copy
N, K=list(map(int,input().split()))
A=list(map(int,input().split()))
B=sorted([(a,abs(a)) for a in A],key=lambda x:x[1],reverse=True)
R=10**9+7
P=1
minus=0
last_neg=-1
last_pos=-1
for i in range(K):
    if B[i][0]>0:
        if last_pos != -1:
            P = (P * B[last_pos][1]) % R
        last_pos=i
    elif B[i][0]<0:
        if last_neg != -1:
            P = (P * B[last_neg][1]) % R
        minus+=1
        last_neg=i
    else:
        print((0))
        return
F=copy.copy(P)
if last_pos!=-1:
    F=(F*B[last_pos][1]) % R
if last_neg!=-1:
    F=(F*B[last_neg][1]) % R
if minus%2==1:
    if K == N:
        print((-F %R))
        return
    first_neg=-1
    first_pos=-1
    count=[0,0]
    for i in range(K,N):
        if count[0]==0 and B[i][0]>0:
            first_pos=i
            count[0]=1
        elif count[1]==0 and B[i][0]<0:
            first_neg=i
            count[1]=1
        elif count==[1,1]:
            break
    if first_pos==-1 and last_pos==-1:
        P = 1
        for i in range(K):
           P = (P * B[N - i - 1][0]) % R
        print(P)
        return
    if first_pos==-1 and first_neg==-1:
        print((0))
        return
    list_product=[]
    if first_neg!=-1 and last_pos!=-1:
        list_product.append(B[last_neg][1]*B[first_neg][1])
    if first_pos!=-1:
        P1=B[first_pos][1]
        if last_pos!=-1:
            P1=P1*B[last_pos][1]
        list_product.append(P1)
    print((max(list_product)*P %R))
else:
    print(F)

