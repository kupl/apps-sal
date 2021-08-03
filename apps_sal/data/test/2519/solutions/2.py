N, K = map(int, input().split())
P = list(map(int, input().split()))
T = [0] * N

for i in range(N):
    P[i] = (1 + P[i]) / 2

if N == K:
    print(sum(P))

else:
    for i in range(1, N):
        P[i] += P[i - 1]

    for i in range(K, N):
        T[i] = P[i] - P[i - K]

    T = T[K:]

    print(max(T))
