(N, K) = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort(reverse=True)
min_h = float('inf')
for i in range(N - K + 1):
    temp = H[i] - H[i + K - 1]
    min_h = min(min_h, temp)
print(min_h)
