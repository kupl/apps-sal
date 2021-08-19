def LI():
    return list(map(int, input().split()))


def MI():
    return map(int, input().split())


def yes():
    return print('Yes')


def no():
    return print('No')


def I():
    return list(input())


def J(x):
    return ''.join(x)


def II():
    return int(input())


def SI():
    return input()


t = II()
for i in range(t):
    (x, y) = MI()
    (a, b) = MI()
    if b > 2 * a:
        print((x + y) * a)
    else:
        c = abs(x - y) * a + min(x, y) * b
        print(c)
