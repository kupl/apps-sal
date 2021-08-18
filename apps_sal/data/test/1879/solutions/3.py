def main():
    ind = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1), '

    t, sx, sy, tx, ty = list(map(int, input().split()))
    s = str(input())

    if sx == tx and sy == ty:
        print('0')
        return

    for i in range(0, t):
        if sx != tx and abs(sx + ind[s[i]][0] - tx) < abs(sx - tx):
            sx += ind[s[i]][0]
        if sy != ty and abs(sy + ind[s[i]][1] - ty) < abs(sy - ty):
            sy += ind[s[i]][1]
        if sx == tx and sy == ty:
            print(i + 1)
            return

    print('-1')


def __starting_point():
    main()


__starting_point()
