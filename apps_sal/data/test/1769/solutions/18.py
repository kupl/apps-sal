mod = 1000000007


def ii():
    return int(input())


def si():
    return input()


def dgl():
    return list(map(int, input()))


def f():
    return map(int, input().split())


def il():
    return list(map(int, input().split()))


def ls():
    return list(input())


uh = ii()
dh = ii()
n = uh + dh + 1
for i in range(uh):
    print(i + 1, end=' ')
print(n, end=' ')
for i in range(n - 1, n - 1 - dh, -1):
    print(i, end=' ')
