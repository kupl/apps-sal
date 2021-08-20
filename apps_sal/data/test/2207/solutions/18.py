from itertools import groupby
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


(n, m) = f()
cnt = 0
x = ''
for i in range(n):
    x = si()
c = 0
for (i, j) in groupby(x):
    c += i == 'B'
print(c)
