def B10N(X,B):
    if X//B!=0: return B10N(X//B,B)+str(X%B)
    return str(X%B)

N,A,B,C = (int(X) for X in input().split())
Li = [int(input()) for X in range(0,N)]
CostM = pow(10,9)
for T in range(0,pow(4,N)):
    Cho = list(B10N(T,4).zfill(N))
    if Cho.count('1')>0 and Cho.count('2')>0 and Cho.count('3')>0:
        Cost = 0
        ALi = [Li[X] for X,Y in enumerate(Cho) if Y=='1']
        BLi = [Li[X] for X,Y in enumerate(Cho) if Y=='2']
        CLi = [Li[X] for X,Y in enumerate(Cho) if Y=='3']
        SyC = (len(ALi)+len(BLi)+len(CLi)-3)*10
        LeC = abs(sum(ALi)-A)+abs(sum(BLi)-B)+abs(sum(CLi)-C)
        if SyC+LeC<CostM: CostM = SyC+LeC
print(CostM)
