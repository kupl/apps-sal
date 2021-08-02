N, K = map(int, input().split())

L = []


for i in range(10**5):
    M = N // K
    if i == 0:
        N = abs(N - K)
        L.append(N)
    else:
        if N > K:
            N = N - (K * M)
            L.append(N)
        else:
            N = abs(L[i - 1] - K)
            L.append(N)


print(min(L))
