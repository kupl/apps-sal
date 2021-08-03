def check(a, b, c, x, y, z):
    ok = True
    ok &= x == max(a, b)
    ok &= y == max(a, c)
    ok &= z == max(b, c)
    return ok


def solve():
    x, y, z = map(int, input().split())
    l = [x, y, z, 1, 10 ** 9]
    for a in l:
        for b in l:
            for c in l:
                if check(a, b, c, x, y, z):
                    print('YES')
                    print(a, b, c)
                    return
    print('NO')


t = int(input())
for _ in range(t):
    solve()
