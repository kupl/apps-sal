N,K=list(map(int,input().split()))
D=[int(x) for x in input().split()]
D=set(D)
kouho=N
while(1):
    lenkouho=len(str(kouho))
    flag=1
    for i in range(lenkouho):
        if int(str(kouho)[i]) in D:
            flag=0
    if flag==1:
        print(kouho)
        break
    kouho+=1

