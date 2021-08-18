
import fileinput


def solve():
    with fileinput.input() as stdin:
        n, d = [int(c) for c in stdin.readline().split(" ")]
        a = [int(c) for c in stdin.readline().split(" ")]
        m = int(stdin.readline())
        a = sorted(a)

        res = 0
        if (m > n):
            res = sum(a)
            res -= (m - n) * d
        else:
            for i in range(m):
                res += a[i]
        print(res)


def __starting_point():
    solve()


__starting_point()
