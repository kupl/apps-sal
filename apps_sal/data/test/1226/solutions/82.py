n, a, b = list(map(int, input().split()))
mod = 10**9+7

def cmb2(n, r, mod):
    res = 1
    temp = 1
    for k in range(1, r+1):
        res *= (n-k+1)
        temp *= k
        res %= mod
        temp %= mod
    res *= pow(temp,(mod-2),mod)
    res %= mod
    return res

def power(a, n, mod):
    bi=str(format(n,"b")) #2進数
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

ans = power(2, n, mod) - cmb2(n, a, mod) - cmb2(n, b, mod) -1
ans %= mod
print(ans)

