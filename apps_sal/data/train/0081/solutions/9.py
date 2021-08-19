t = int(input())


def test():
    a = input().strip()
    b = input().strip()
    c = input().strip()
    for (x, y, z) in zip(a, b, c):
        if z != x and z != y:
            print('NO')
            return
    print('YES')


for _ in range(t):
    test()
