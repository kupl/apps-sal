import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(X, Y) = lr()
if abs(Y - X) >= 2:
    print('Alice')
else:
    print('Brown')
