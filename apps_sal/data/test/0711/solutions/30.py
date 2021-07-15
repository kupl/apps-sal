N,M=map(int,input().split())
mod=10**9+7
 
def nCmMOD(A,B,Mod):
    num,den=1,1
    for i in range(B):
        num*=(A-i)
        den*=(i+1)
        num%=Mod
        den%=Mod
    return (num*pow(den,Mod-2,Mod))%Mod
 
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
 
ans=1
F=factorization(M)
for i in range(len(F)):
    f=F[i][1]
    ans*=nCmMOD(f+N-1,N-1,mod)
    ans%=mod
 
if M==1:
    print(1)
else:
    print(ans)
