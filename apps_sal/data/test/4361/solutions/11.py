N, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

result = 10 ** 9
for i in range(N - K + 1):
    result = min(result, T[i + K - 1] - T[i])

print(result)
