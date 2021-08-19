import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

grid = [[0 for _ in range(W)] for _ in range(H)]
point = A[0]
color = 0
for i in range(H):
    for j in range(W):
        # 色iが接するように、左 -> 右 -> 下の列を右から、と染めていく
        if i % 2 == 0:
            x = j
        else:
            x = W - j - 1
        if point == 0:
            color += 1
            point = A[color]

        grid[i][x] = color + 1
        point -= 1

for i in range(H):
    print(*grid[i])
