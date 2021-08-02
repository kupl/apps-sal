H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
now = 0
grid = [0] * (H * W)

for i in range(N):
    for j in range(now, now + a[i]):
        grid[j] = i + 1
    now += a[i]

reverse = 0

for k in range(0, H * W, W):
    if reverse:
        print(*grid[k + W - 1:k - 1:-1])
        reverse = 0
    else:
        print(*grid[k:k + W])
        reverse = 1
