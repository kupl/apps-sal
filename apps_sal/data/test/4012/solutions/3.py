import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


f = [[] for i in range(20021)]

for i in range(1, 20021):
    for j in range(1, i + 1):
        if j * j > i:
            break
        if i % j == 0:
            f[i].append(j)
            if j * j != i:
                f[i].append(i // j)


def solve():
    a, b, c = mints()
    ans = (int(1e9), 0, 0, 0)
    for C in range(1, 2 * c + 10):
        dc = abs(C - c)
        for B in f[C]:
            db = abs(B - b)
            for A in f[B]:
                ans = min(ans, (dc + db + abs(A - a), A, B, C))
    print(ans[0])
    print(*ans[1:])


for i in range(mint()):
    solve()
