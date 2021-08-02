N, K = map(int, input().split())
ans = 0
for p in range(K + 1, N + 1):
    k = N // p
    l = N % p
    a = k * (p - K) + max(l - K + 1, 0)
    if(K == 0):
        a -= 1
    ans += a
print(ans)
