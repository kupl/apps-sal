import sys


def solve():
    (n, k) = map(int, input().split())
    bada = list(map(int, input().split()))
    a = list()
    for i in range(len(bada)):
        if len(a) > 0 and bada[i] == a[-1]:
            continue
        a.append(bada[i])
    bad = [0] * (k + 1)
    for (i, val) in enumerate(a):
        if i + 1 >= len(a) and i == 0:
            continue
        if i + 1 >= len(a):
            bad[val] += 1
        elif i == 0:
            bad[val] += 1
        else:
            before = a[i - 1]
            after = a[i + 1]
            bad[val] += 2 if before == after else 1
    which = -1
    howmany = -1
    for i in range(len(bad)):
        if bad[i] > howmany:
            which = i
            howmany = bad[i]
    print(which)


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
