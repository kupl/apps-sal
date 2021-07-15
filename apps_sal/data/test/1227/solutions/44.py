def f(N,K):
    n=len(str(N))
    if n==1:
        if K==1:
            return N
        else:
            return 0
    elif n==2:
        if K==1:
            return 9+N//10
        elif K==2:
            return N-9-N//10
        else:
            return 0
    elif n==3:
        if K==1:
            return 18+N//100
        elif K==2:
            return 81+18*((N//100)-1)+f(N%100,1)
        else:
            return 81*((N//100)-1)+f(N%100,2)
    else:
        if K==1:
            return 9*(n-1)+N//(10**(n-1))
        elif K==2:
            return 81*(n-1)*(n-2)/2+9*(n-1)*((N//((10**(n-1))))-1)+f(N%(10**(n-1)),1)
        else:
            return 243*(n**3-6*(n**2)+11*n-6)/2+81*(n-1)*(n-2)*((N//(10**(n-1)))-1)/2+f(N%(10**(n-1)),2)
N=int(input())
K=int(input())
print(int(f(N,K)))
