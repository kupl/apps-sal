arr = [[int(i) % 2 for i in input().split()] for _ in range(3)]
state = [[1] * 3 for i in range(3)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for y in range(3):
    for x in range(3):
        state[y][x] ^= arr[y][x]
        for dy, dx in dirs:
            j, i = y + dy, x + dx
            if 0 <= j < 3 and 0 <= i < 3:
                state[y][x] ^= arr[j][i]
for row in state:
    print(*row, sep='')
