L=[0]+list(map(int,input().split()))
S=sum(L)
if S%2==1:
    print("No")
    return

D=[{}for i in range(5)]
D[0][0]=1
for i in range(1,5):
    for k,v in list(D[i-1].items()):
        D[i][k]=1
        D[i][k+L[i]]=1
if S//2 in D[-1]:
    print("Yes")
else:
    print("No")

