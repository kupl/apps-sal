N,K = map(int, open(0).read().split())
ans = 0
if K == 0:
    print(pow(N,2))
else:
    for b in range(K+1,N+1):
        d, m = divmod(N,b)
        ans += d * (b-K) + max(0,(m-K+1))
    print(ans)
