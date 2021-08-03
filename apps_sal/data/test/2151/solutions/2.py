def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


for q in range(ii()):
    n = ii()
    s = input().strip()
    a, b = int(s[0]), int(s[1:])
    if a >= b:
        print('NO')
    else:
        print('YES')
        print(2)
        print(a, b)
