(N, K) = map(int, input().split())
A = [int(a) for a in input().split()]
mod = 10 ** 9 + 7
P = []
M = []
z = 0
for a in A:
    if a > 0:
        P.append(a)
    elif a < 0:
        M.append(a)
    else:
        z += 1
P.sort()
M.sort()
ans = 1
if len(M) == 0 or N == K:
    A.sort(reverse=True)
    for i in range(K):
        ans *= A[i]
        ans %= mod
elif len(P) == 0:
    if K % 2 == 0 and len(M) >= K:
        for i in range(K):
            ans *= M[i]
            ans %= mod
    elif K % 2 == 1 and z == 0:
        for i in range(-1, -K - 1, -1):
            ans *= M[i]
            ans %= mod
    else:
        ans = 0
elif N - z < K or (N - z == K and len(M) % 2 == 1):
    ans = 0
else:
    L = []
    for i in range(N):
        if A[i] == 0:
            continue
        L.append((abs(A[i]), A[i]))
    L.sort(reverse=True)
    cnt = 0
    lp = -1
    lm = -1
    for i in range(K):
        if L[i][1] > 0:
            lp = i
        else:
            lm = i
            cnt += 1
        ans *= L[i][0]
        ans %= mod
    if cnt % 2 == 1:
        p = -1
        m = -1
        for i in range(K, len(L)):
            if p > 0 and m > 0:
                break
            if L[i][1] > 0 and p < 0:
                p = L[i][0]
            elif L[i][1] < 0 and m < 0:
                m = L[i][0]
        if p < 0:
            ans *= m * pow(L[lp][0], mod - 2, mod)
        elif m < 0:
            ans *= p * pow(L[lm][0], mod - 2, mod)
        elif lp >= 0 and L[lm][0] * m > L[lp][0] * p:
            ans *= m * pow(L[lp][0], mod - 2, mod)
        else:
            ans *= p * pow(L[lm][0], mod - 2, mod)
        ans %= mod
print(ans)
