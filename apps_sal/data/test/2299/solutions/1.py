import sys


def debug(x, table):
    for (name, val) in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    (n, m) = map(int, sys.stdin.readline().split())
    A = [[int(i) for i in sys.stdin.readline().split()] for j in range(n)]
    q = int(sys.stdin.readline().rstrip())
    querys = [tuple(map(int, sys.stdin.readline().split())) for i in range(q)]
    f = [i for i in range(n)]
    for j in range(m):
        s = 0
        for i in range(n):
            if i == n - 1 or A[i][j] > A[i + 1][j]:
                for k in range(s, i + 1):
                    f[k] = max(f[k], i)
                s = i + 1
    ans = []
    for (l, r) in querys:
        if r - 1 <= f[l - 1]:
            ans.append('Yes')
        else:
            ans.append('No')
    print(*ans, sep='\n')


def __starting_point():
    solve()


__starting_point()
