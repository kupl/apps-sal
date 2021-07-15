import sys

def solve():
    n, m = map(int, input().split())

    for i in range(m):
        k, *a = [int(j) for j in input().split()]
        a.sort(key=abs)
        # print(a)

        if k == 1:
            print('YES')
            return

        for j in range(len(a) - 1):
            if a[j] == -a[j + 1]:
                break
        else:
            print('YES')
            return

    print('NO')

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def __starting_point():
    solve()
__starting_point()
