# C - Christmas Eve
N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h = sorted(h, reverse=True)

diff = 10**9
for i in range(N - K + 1):
    a = h[i] - h[i + K - 1]
    if diff > a:
        diff = a
    if diff == 0:
        break
print(diff)
