def main():
    n, k = list(map(int, input().split()))
    l = [['0'] * n for _ in range(n)]
    for y, row in enumerate(l):
        if not k:
            break
        k -= 1
        row[y] = '1'
        for x in range(y + 1, n):
            if k < 2:
                break
            k -= 2
            l[x][y] = row[x] = '1'
    if k:
        print(-1)
    else:
        for row in l:
            print(' '.join(row))


def __starting_point():
    main()


__starting_point()
