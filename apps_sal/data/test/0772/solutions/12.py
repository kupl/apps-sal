def main():
    l = [list(map(int, input().strip().split())) for _ in range(3)]
    field = [[1] * 3 for _ in range(3)]
    for y in range(3):
        for x in range(3):
            if l[y][x] & 1:
                for i in range(max(y - 1, 0), min(y + 2, 3)):
                    field[i][x] ^= 1
                for j in range(max(x - 1, 0), min(x + 2, 3)):
                    field[y][j] ^= 1
                field[y][x] ^= 1
    for _ in range(3):
        print(''.join(map(str, field[_])))


main()
