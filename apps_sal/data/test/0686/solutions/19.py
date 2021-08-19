def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


t = rint()
for _ in range(t):
    (x, y) = rints()
    print('YES' if x - y > 1 else 'NO')
