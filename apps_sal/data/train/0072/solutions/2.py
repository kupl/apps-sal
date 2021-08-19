import sys
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def solve():
    (n, k) = nm()
    a = nl()
    if k < len(set(a)):
        print(-1)
        return
    f = list(set(a))
    f += [1] * (k - len(f))
    f *= n
    print(len(f))
    print(*f)
    return


t = ni()
for _ in range(t):
    solve()
