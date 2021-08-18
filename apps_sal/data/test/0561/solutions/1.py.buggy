__author__ = 'asmn'
n = int(input())
a = sorted(map(int, input().split()))

# print('begin')


def checked(a, d):
    for i in range(1, len(a)):
        if a[i] - a[i - 1] != d:
            return False
    return True


td = None


def canfix(a):
    a = sorted(a[i] - a[i - 1] for i in range(1, len(a)))
    if a[-1] != a[0] * 2:
        return False
    elif sum(a) != a[0] * (len(a) + 1):
        return False
    else:
        nonlocal td
        td = a[0]
        return True


def fix(a, d):
    for i in range(1, len(a)):
        if a[i] - a[i - 1] != d:
            return a[i] - d


if n == 1:
    print(-1)
elif n == 2:
    if sum(a) % 2 == 0:
        if a[0] == a[1]:
            print(1)
            print(a[0])
        else:
            print(3)
            print(*(2 * a[0] - a[1], sum(a) // 2, 2 * a[1] - a[0]))
    else:
        print(2)
        print(*(2 * a[0] - a[1], 2 * a[1] - a[0]))
else:
    d = a[1] - a[0]
    if checked(a, d):
        if d == 0:
            print(1)
            print(a[0])
        else:
            print(2)
            print(a[0] - d, a[-1] + d)
    elif canfix(a):
        print(1)
        print(fix(a, td))
    else:
        print(0)
