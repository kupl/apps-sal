n,m,k=map(int,input().split())
mod=998244353
ans=0

fact=[1] * (n+1)  # 階乗を格納するリスト
factinv=[1] * (n+1)  # 階乗を格納するリスト
for i in range(n):
    fact[i+1] = fact[i] * (i+1) % mod  # 階乗を計算
    factinv[i+1] = pow(fact[i+1], mod-2, mod)  # modを法とした逆元（フェルマーの小定理）

def nCk(n,k):  # 組み合わせ(mod)を返却する
    return fact[n] * factinv[n-k] * factinv[k] % mod

for k_i in range(k+1):
    ans += m * pow(m-1, n-1-k_i, mod) * nCk(n-1, k_i)
    ans %= mod
print (ans)
