import sys


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    n, l, r = map(int, input().split())
    bit_len = len(bin(n)[2:])
    cnt = 0

    for i in range(l, r + 1):
        off = bit_len - 1
        for j in range(bit_len - 1):
            if i & (1 << j):
                break
            else:
                off -= 1
        cnt += (n >> off) & 1

    print(cnt)


def __starting_point():
    solve()


__starting_point()
