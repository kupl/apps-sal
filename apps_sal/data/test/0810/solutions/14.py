fact = [1]
mod = 10**9 + 7
def factorial(n):
    nonlocal  mod
    nonlocal  fact
    fact = [1]
    mod = 10**9 + 7
    for i in range(1,n+1):
        fact.append(fact[-1] * i)
        fact[-1] %= mod
def C(n,k):
    nonlocal mod
    return  (((fact[n]*pow(fact[k],mod-2,mod))%mod)*pow(fact[n-k],mod-2,mod))%mod
def good(x,a,b):
    while x > 0:
        if(x%10!=a and x%10!=b):
            return  False
        x//=10
    return  True
for _ in range(1):
    ans = 0
    a,b,n = map(int,input().split())
    factorial(n)
    for i in range(n+1):
        if(good(i*a+(n-i)*b,a,b)):
            ans += C(n,i)
            ans %= mod
    print(ans)
