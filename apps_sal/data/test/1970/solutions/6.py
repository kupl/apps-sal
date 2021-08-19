def main():
    n = int(input())
    out = ''
    for t in range(n):
        knights = [0 for i in range(16)]
        valid = [False for i in range(16)]
        for i in range(8):
            line = input()
            for j in range(8):
                if line[j] != '#':
                    valid[get(i, j)] = True
                if line[j] == 'K':
                    knights[get(i, j)] += 1
        for i in range(16):
            if knights[i] == 2 and valid[i]:
                out += 'YES\n'
                break
        else:
            out += 'NO\n'
        if t != n - 1:
            input()
    print(out[:-1])


def get(i, j):
    return [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]][i % 4][j % 4]


def __starting_point():
    main()


__starting_point()
