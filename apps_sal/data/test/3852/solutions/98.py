import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))
n = int(input())
a = list(map(int, input().split()))
m = max([abs(item) for item in a if item <= 0] + [0])
M = max([abs(item) for item in a if item >= 0] + [0])


def sub(i, j, a):
    print(i, j)
    a[j - 1] += a[i - 1]


print(2 * n - 1)
if M >= m:
    ind = a.index(M) + 1
    for i in range(1, n + 1):
        if i == ind:
            continue
        sub(ind, i, a)
    sub(ind, 1, a)
    for i in range(1, n):
        sub(i, i + 1, a)
else:
    ind = a.index(-m) + 1
    for i in range(1, n + 1):
        if i == ind:
            continue
        sub(ind, i, a)
    sub(ind, n, a)
    for i in range(n, 1, -1):
        sub(i, i - 1, a)
