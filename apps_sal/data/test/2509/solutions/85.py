N, K = list(map(int, input().split()))
if K == 0:
    print(N**2)
else:
    res = 0
    for b in range(1, N+1):
        L = max(b-K, 0)
        res += L*(N//b) + max(0, (N%b)+1-K)

    print(res)
