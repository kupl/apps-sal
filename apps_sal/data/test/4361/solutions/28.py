N, K = list(map(int, input().split()))
h = [int(input()) for i in range(N)]
h.sort(reverse=True)
minimum = 10**9
for i in range(N - K + 1):
    minimum = min(minimum, h[i] - h[i + K - 1])
print(minimum)
