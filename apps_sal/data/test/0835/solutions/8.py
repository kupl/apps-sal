def Divide(a,b):
    if(b==0):
        return 10**100
    return a//b
def main():
    s=input()

    Nb,Ns,Nc=list(map(int,input().split()))

    Pb,Ps,Pc=list(map(int,input().split()))

    r=int(input())

    B=s.count('B')
    S=s.count('S')
    C=s.count('C')

    needed=B*Pb+C*Pc+S*Ps
    ans=0
    while(1):
        x=needed
        if(Nb!=0):
            if(Nb>B):
                x-=B*Pb
                Nb-=B
            else:
                x-=Nb*Pb
                Nb=0
        if(Nc!=0):
            if(Nc>C):
                x-=C*Pc
                Nc-=C
            else:
                x-=Nc*Pc
                Nc=0
        if(Ns!=0):
            if(Ns>S):
                x-=S*Ps
                Ns-=S
            else:
                x-=Ns*Ps
                Ns=0
        if(x<=r):
            r-=x
            ans+=1
        else:
            break
        if((Nb==0 or B==0) and (Nc==0 or C==0) and (Ns==0 or S==0)):
            break
    ans+=r//needed
    print(ans)
    return

    
main()
    

