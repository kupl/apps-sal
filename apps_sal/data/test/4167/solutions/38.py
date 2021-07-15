N, K = list(map(int, input().split()))

# 1以上N以下で、Kで割った余りが0,1,...,K-1となる個数
l = [0] * K
for i in range(1, N + 1):
    l[i % K] += 1

ans = 0

# aをKで割った余りは0,1,...,K-1
for ai in range(K):
    # bをKで割った余り...(a+b)%K==0から   cをKで割った余り...(a+c)%K==0から
    # ai = 0の時にK-aiがKとなって「余り」として不適なので%をかける
    bi = (K - ai) % K
    ci = (K - ai) % K
    # (b+c)%K==0を満たせば良い
    if (bi + ci) % K == 0:
        ans += l[ai] * l[bi] * l[ci]
print(ans)

