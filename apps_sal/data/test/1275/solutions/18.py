N, K = list(map(int, input().split()))
count = 0

for x in range(2, min(2 * N + 1, K + 2 * N + 1)):
    x_way = min(N, x - 1) - max(1, x - N) + 1
    y = x - K
    if 2 <= y <= 2 * N:
        y_way = min(N, y - 1) - max(1, y - N) + 1
        count += x_way * y_way

print(count)
