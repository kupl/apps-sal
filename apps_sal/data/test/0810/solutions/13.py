from math import factorial as fct 

MOD = 10**9 + 7
def c(n,k):
    return fct(n)//(fct(k)*fct(n-k))
 
def check(val,a,b):
    while val>0 :
        if val%10 == a or val%10 == b:
            val = val//10
        else:
            return False
    return True

a,b,n = list(map(int,input().split()))
f = [1]
for i in range(1, n + 1):
    f.append(f[-1] * i % MOD)
ans = 0

for i in range(n+1):
    if check(i*a + (n-i)*b,a,b):
        ans += pow(f[i]*f[n-i],MOD-2,MOD)
        ans %= MOD

print((ans*f[n])%MOD)

