(R, C) = list(map(int, input().split()))
field = []
for i in range(R):
    line = input()
    f = []
    for ch in line:
        f.append(ch)
    field.append(f)
lu = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def main():
    for i in range(R):
        for j in range(C):
            item = field[i][j]
            if item == '.':
                field[i][j] = 'D'
            if item == 'S':
                for [di, dj] in lu:
                    di += i
                    dj += j
                    if di in range(R) and dj in range(C):
                        if field[di][dj] == 'W':
                            print('No')
                            return
    print('Yes')
    for line in field:
        print(''.join(line))


main()
