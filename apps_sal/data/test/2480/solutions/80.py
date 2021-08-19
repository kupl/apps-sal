(N, K) = map(int, input().split())
L = list(map(int, input().split()))
R = list()
if K >= N:
    sums = 0
    c = dict()
    for i in range(N):
        sums += L[i]
        sums %= K
        a = (sums - i - 1) % K
        if a in c:
            c[a] += 1
        else:
            c[a] = 1
    ans = 0
    for i in c:
        ans += (c[i] - 1) * c[i] // 2
    if 0 in c:
        print(ans + c[0])
    else:
        print(ans)
else:
    ans = 0
    c = [0] * K
    sums = 0
    for i in range(N):
        sums += L[i]
        sums %= K
        a = (sums - i - 1) % K
        R.append(a)
    for i in range(K - 1):
        c[R[i]] += 1
    ans += c[0]
    c[R[K - 1]] += 1
    for i in range(N):
        if i < N - K:
            ans += c[R[i]] - 1
            c[R[i]] -= 1
            c[R[i + K]] += 1
        else:
            ans += c[R[i]] - 1
            c[R[i]] -= 1
    print(ans)
