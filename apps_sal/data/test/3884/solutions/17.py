import sys


def __starting_point():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    eps = 2e-07
    (off, land) = ([], [])
    off = list(map(int, sys.stdin.readline().strip().split(' ')))
    land = list(map(int, sys.stdin.readline().strip().split(' ')))
    if 1 in off or 1 in land:
        print(-1)
    else:
        (l, r) = (0, 10 ** 9)

        def is_ok(target):
            total = m + target
            remain = total
            for i in range(n):
                remain -= remain / off[i]
                if remain < m and abs(remain - m) > eps:
                    return False
                remain -= remain / land[(i + 1) % n]
                if remain < m and abs(remain - m) > eps:
                    return False
            return True
        while True:
            mid = (l + r) / 2
            if abs(r - l) <= eps:
                print(mid)
                break
            if is_ok(mid):
                r = mid
            else:
                l = mid


__starting_point()
