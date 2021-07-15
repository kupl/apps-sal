c1,c2,c3,c4=list(map(int,input().split()))

n,m=list(map(int,input().split()))
B=list(map(int,input().split()))

T=list(map(int,input().split()))

if(sum(B)==0):
    C=0
    for item in T:
        if(item*c1>c2):
            C+=c2
        else:
            C+=item*c1
    print(min((C,c4,c3)))

elif(sum(T)==0):
    C=0
    for item in B:
        if(item*c1>c2):
            C+=c2
        else:
            C+=item*c1
    print(min((C,c4,c3)))

else:
    A=0
    for item in T:
        if(item*c1>c2):
            A+=c2
        else:
            A+=item*c1
    Q=0
    for item in B:
        if(item*c1>c2):
            Q+=c2
        else:
            Q+=item*c1
    print(min((A+Q,c3+c3,c4,A+c3,Q+c3)))
        

