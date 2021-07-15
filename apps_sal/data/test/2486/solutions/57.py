import sys

def biser(lst,func):
    n=len(lst)
    nh=n//2
    if n==1:
        if func(lst[0]):
            return lst[0]
        else:
            return -1
    if func(lst[nh]):
        return biser(lst[nh:],func)
    else:
        return biser(lst[:nh],func)

def mkns(a,s,m):
    if a==0:
        return s
    else:
        return (((s+1)<<a)|s) & m

def main():
    N,K=list(map(int,sys.stdin.readline().strip().split()))
    a=list(map(int,sys.stdin.readline().strip().split()))
    a.sort()
    ss=[0]*(N+1)
    pm=(1<<K)-1
    mask=lambda c:(1<<K)-(1<<c)
    nn=0
    def isunnec(i):
        if a[i]>=K:
            return False
        for j in range(i+1,N):
            if a[j]>=K:
                break
            ss[i]=(((ss[i]+1)<<a[j])|ss[i]) & pm
        if ss[i]&mask(K-a[i])==0:
            return True
        return False
    
    for i in range(N):
        if a[i]>=K:
            break
        ss[i+1]=(((ss[i]+1)<<a[i])|ss[i]) & pm
    nn=biser(list(range(N)),isunnec)+1
    print(nn)

def __starting_point():
    main()

__starting_point()
