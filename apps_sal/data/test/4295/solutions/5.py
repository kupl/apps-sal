[N, K] = list(map(int, input().split(' ')))
N = N % K
nN = abs(N - K)
while nN < N:
    N = nN
    nN = abs(N - K)
print(N)
