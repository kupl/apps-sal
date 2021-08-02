import sys


def otb(l):
    i = 0
    while i < n - 1:
        if l[i] - 1 == l[i + 1]:
            l[i] -= 1
            i += 1
        elif l[i] == l[i + 1]:
            i += 1
        i += 1
    znach = []
    i = 0
    while i < n - 1:
        if l[i] == l[i + 1]:
            znach.append(l[i])
            i += 1
        i += 1
    return znach


def ploshad(n, znach):
    summa = 0
    n = len(znach)
    for i in range(0, n - 1, 2):
        summa += znach[i] * znach[i + 1]
    sys.stdout.write(str(summa))


n = int(sys.stdin.readline())
l = []
l = [int(j) for j in sys.stdin.readline().split()]
l.sort(reverse=True)
znach = otb(l)
ploshad(n, znach)
