(N, K) = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()
res = 10 ** 9
for i in range(N - K + 1):
    res = min(res, H[i + K - 1] - H[i])
print(res)
