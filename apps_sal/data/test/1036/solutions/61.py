import sys
from functools import reduce

zz = 1

sys.setrecursionlimit(10**5)
if zz:
    input = sys.stdin.readline
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('all.txt', 'w')
di = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def fori(n):
    return [fi() for i in range(n)]


def inc(d, c, x=1):
    d[c] = d[c] + x if c in d else x


def ii():
    return input().rstrip()


def li():
    return [int(xx) for xx in input().split()]


def fli():
    return [float(x) for x in input().split()]


def comp(a, b):
    if(a > b):
        return 2
    return 2 if a == b else 0


def gi():
    return [xx for xx in input().split()]


def gtc(tc, ans):
    print(("Case #" + str(tc) + ":", ans))


def cil(n, m):
    return n // m + int(n % m > 0)


def fi():
    return int(input())


def pro(a):
    return reduce(lambda a, b: a * b, a)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def si():
    return list(input().rstrip())


def mi():
    return list(map(int, input().split()))


def gh():
    sys.stdout.flush()


def isvalid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def bo(i):
    return ord(i) - ord('a')


def graph(n, m):
    for i in range(m):
        x, y = mi()
        a[x].append(y)
        a[y].append(x)


t = 1
uu = t
w = {"PS": "S", "PR": "P", "RS": "R"}


def winner(s, p):
    if s == p:
        return s
    return w["".join(sorted(s + p))]


dp = {}


def rec(i, j):
    if j == 0:
        dp[i, j] = s[i]
        return dp[i, j]
    if (i, j) in dp:
        return dp[i, j]
    dp[i, j] = winner(rec(i, j - 1), rec((i + pow(2, j - 1, n)) % n, j - 1))
    return dp[i, j]


while t > 0:
    t -= 1
    n, k = mi()
    s = ii()
    print((rec(0, k)))
