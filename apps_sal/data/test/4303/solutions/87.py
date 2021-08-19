(N, K) = list(map(int, input().split()))
D = [int(n) for n in input().split()]
ans = 10000000000
for i in range(N - K + 1):
    L = D[i]
    R = D[i + K - 1]
    LR = abs(L) + abs(L - R)
    RL = abs(R) + abs(R - L)
    ans = min(ans, min(LR, RL))
print(ans)
