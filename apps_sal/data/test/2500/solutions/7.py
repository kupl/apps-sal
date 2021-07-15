P=10**9+7
inv2=(1+P)//2
def exp(a,k):
    if k==0:
        return 1
    elif k%2==0:
        return (exp(a*a,k//2))%P
    else:
        return (a*exp(a*a,k//2))%P
D=dict()
def f(N):
    if N in D:
        return D[N]
    if N<=1:
        D[N]=N
        return N
    i=0
    while(1):
        if 2**i<=N<2**(i+1):
            break
        i+=1
    if N==2**i:
        D[N]=((1+exp(3,i))*inv2)%P
        return D[N]
    D[N]=(f(N-2**i)-f(2**(i+1)-N-1)+exp(3,i))%P
    return D[N]
print(f(int(input())+1))
