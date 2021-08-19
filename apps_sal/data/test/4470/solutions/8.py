def ain():
    return map(int, input().split())


def lin():
    return list(ain())


def plist(l):
    for x in l:
        print(x, end=' ')
    print()


def indexof(l, v, l3):
    return l3[v]


for _ in range(int(input())):
    n = int(input())
    c = 0
    f = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = 2 * n // 3
        elif n % 5 == 0:
            n = 4 * n // 5
        else:
            f = 1
            print(-1)
            break
        c += 1
    if f == 0:
        print(c)
