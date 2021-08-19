import sys
sys.setrecursionlimit(10 ** 8)


def ii():
    return int(sys.stdin.readline())


def mi():
    return map(int, sys.stdin.readline().split())


def li():
    return list(map(int, sys.stdin.readline().split()))


def li2(N):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def dp2(ini, i, j):
    return [[ini] * i for _ in range(j)]


N = ii()
ans = ''


def div(a, b=-2):
    if a >= 0:
        return (-(a // -b), a % -b)
    elif -a % -b == 0:
        return (-a // -b, 0)
    else:
        return (-a // -b + 1, 1)


while True:
    (N, m) = div(N)
    ans += str(m)
    if abs(N) < 2:
        break
if N == -1:
    ans += '11'
elif N == 1:
    ans += '1'
print(ans[::-1])
