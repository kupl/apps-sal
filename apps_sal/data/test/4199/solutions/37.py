N,K=list(map(int,input().split()))
h=input()

def ans142(N:int, K:int, h:list):
    N=int(N)
    K=int(K)
    count=0
    if N==1:
        h=int(h)
        if h>=K:
           return(1)
        elif h<K:
           return(0)
    else:
     h=h.split()
     for i in range(0,N):
        if int(h[i])>=K:
            count+=1
     return(count)
print((ans142(N,K,h)))

