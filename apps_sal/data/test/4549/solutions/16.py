(H, W) = map(int, input().split())
S = [['.'] * (W + 2)]
for i in range(H):
    S.append(list('.' + input().rstrip() + '.'))
S.append(['.'] * (W + 2))


def checkaround(i, j):
    dirc = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    for d in dirc:
        if S[i - d[0]][j - d[1]] == '#':
            return True
    return False


def main():
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if S[i][j] == '#':
                if not checkaround(i, j):
                    print('No')
                    return
    print('Yes')


main()
