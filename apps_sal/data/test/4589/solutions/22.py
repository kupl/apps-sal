H, W = [int(i) for i in input().split()]
SS = [input() for _ in range(H)]


def s(y, x):
    if x >= W or x < 0 or y >= H or y < 0:
        return 0

    return 1 if SS[y][x] == '


for i in range(H):
    S = SS[i]
    l = []
    for j in range(W):
        c = S[j]
        if c == '.':
            l.append(str(sum([s(i - 1, j - 1), s(i - 1, j), s(i - 1, j + 1), s(i, j - 1), s(i, j + 1), s(i + 1, j - 1), s(i + 1, j), s(i + 1, j + 1)])))
        else:
            l.append('
    print((''.join(l)))
