class Factorial:
    def __init__(self,n,mod):
        self.f=f=[0]*(n+1)
        f[0]=b=1
        self.mod=mod
        for i in range(1,n+1):f[i]=b=b*i%mod
        self.inv=inv=[0]*(n+1)
        inv[n]=b=pow(self.f[n],mod-2,mod)
        for i in range(n,0,-1):inv[i-1]=b=b*i%mod
    def factorial(self,i):
        return self.f[i]
    def ifactorial(self,i):
        return self.inv[i]
    def comb(self,n,k):
        if n>=k:
            return self.f[n]*self.inv[n-k]%self.mod*self.inv[k]%self.mod
        else:
            return 0
M=10**9+7
a,b,c,d=map(int,input().split())
comb=Factorial(c+d+2,M).comb
f=lambda r,c:comb(c+r+2,r+1)-c-r-2
print((f(c,d)-f(c,b-1)-f(a-1,d)+f(a-1,b-1))%M)
