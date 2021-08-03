N, M, K = list(map(int, input().split()))
row_size = 2 * M
K -= 1
row = K // row_size
K %= row_size
side = 'L' if K % 2 == 0 else 'R'
d = K // 2

print(row + 1, d + 1, side)
