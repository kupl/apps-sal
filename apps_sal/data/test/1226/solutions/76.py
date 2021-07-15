n,a,b=map(int,input().split())

def genCombinationFunction(max_k,mod):
    modinv_table = [-1] * (max_k+1)
    modinv_table[1] = 1
    for i in range(2, max_k+1):
        modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

    def binomial_coefficients(n, k):
        ans = 1
        for i in range(k):
            ans *= n-i
            ans *= modinv_table[i + 1]
            ans %= mod
        return ans
    return binomial_coefficients

  
max_k = 2 * 10 ** 5
mod = 10**9 + 7
f=genCombinationFunction(max_k,mod)


ans=pow(2,n,mod)-1
ans-=f(n,a)
ans-=f(n,b)
print(ans%mod)
