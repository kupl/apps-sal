import math
N = int(input())

def factrize(N):
    L={}
    for n in range(2,N+1):
        L[n]=0
        while N % n == 0:
            L[n]+=1
            N = N/n
    return L

f_ = {}
for n in range(2,int(N)+1):
    f_[n]=0
        
for n in range(1,N+1):
    F=factrize(n)
    for f in F.keys():
        f_[f]+=F[f]
        
ans=1
for f in f_.keys():
    if f_[f] != 0:
        ans=ans*(f_[f]+1)
        
print(ans%((10**9)+7))
