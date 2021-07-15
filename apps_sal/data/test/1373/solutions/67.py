def resolve():
    n, k = map(int,input().split())
    a = 10**9+7
    ans =0
    for K in range(k,n+2):
        ans += n*K - K**2 + K + 1
        ans %= a
    print(ans)
resolve()
