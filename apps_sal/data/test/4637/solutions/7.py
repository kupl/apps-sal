import math


def ri():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


def inp():
    return int(input())


def si():
    return input()


def pYes():
    print("YES")


def pNo():
    print("NO")


def plist(l):
    print("".join(l))


t = int(input())
for i in range(t):
    n, k = ri()
    a = li()
    b = li()
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
        else:
            break
    print(sum(a))
