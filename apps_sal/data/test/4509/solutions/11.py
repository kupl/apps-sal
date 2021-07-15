for _ in range(int(input())):
    n,k=map(int,input().split())
    lo=0 
    hi=10**20
    def check(mi):
        return mi-mi//n>=k 
    while lo<=hi:
        mi=(lo+hi)//2 
        if check(mi):
            ans=mi 
            hi=mi-1 
        else:
            lo=mi+1 
    print(ans)
