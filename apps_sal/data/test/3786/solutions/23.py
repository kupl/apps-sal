import sys
import bisect


def Ri():
    return [int(x) for x in sys.stdin.readline().split()]


def ri():
    return sys.stdin.readline().strip()


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


INF = 10 ** 30
MOD = 998244353
n = int(ri())
a = Ri()
dic = {}
for i in range(len(a)):
    if a[i] == 1:
        dic[i + 2] = 1
    else:
        time = dic[a[i]]
        dic[i + 2] = time + 1
cnt = 0
time = {}
for i in dic:
    if dic[i] in time:
        time[dic[i]] += 1
    else:
        time[dic[i]] = 1
for i in time:
    cnt += time[i] % 2
print(cnt + 1)
