def S(n):
    k=list(str(n))
    import functools
    return functools.reduce(lambda x,y:x+y,[int(i) for i in k])
k=int(input())
def T(n):
    return n/S(n)
def f(N):
    len_N=len(str(N))
    A=[10**len_N+10**i-1 for i in range(len_N)]
    B=[T(i) for i in A]
    ans1=A[B.index(min(B))]
    i=0
    while True:
        I=10**(len_N-1)+10**i-1
        J=10**(len_N-1)+10**(i+1)-1
        if T(J)<T(I):
            i+=1
        else:
            break
    C=[((N+1)//(10**i))*10**i+j*10**i-1 for j in range(1,11)]
    D=[T(i) for i in C]
    ans2=C[D.index(min(D))]
    if T(ans1)<T(ans2):
        return(ans1)
    else:
        return(ans2)
K=[]
N=1
while len(K)<k:
    K.append(N)
    N=f(N)
for i in range(k):
    print((K[i]))

