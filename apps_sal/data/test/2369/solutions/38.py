(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
m = 10 ** 9 + 7
alpha = 1
beta = 1
for i in range(1, K):
    alpha *= N - i
    beta *= i
    alpha %= m
    beta %= m
gamma = alpha * pow(beta, m - 2, m) % m
ans = 0
for i in range(N - K + 1):
    minA = A[i]
    maxA = A[N - 1 - i]
    ans = (ans + gamma * (maxA - minA)) % m
    gamma = gamma * pow(N - 1 - i, m - 2, m) * (N - K - i) % m
print(ans)
