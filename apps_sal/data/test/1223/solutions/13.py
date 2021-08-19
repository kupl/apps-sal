import sys
import bisect as bs
import collections as cl
sys.setrecursionlimit(100000)
mod = 10**9 + 7
Max = sys.maxsize


def l():  # intのlist
    return list(map(int, input().split()))


def m():  # 複数文字
    return list(map(int, input().split()))


def onem():  # Nとかの取得
    return int(input())


def s(x):  # 圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x) - 1):
        if aa != x[i + 1]:
            a.append([aa, su])
            aa = x[i + 1]
            su = 1
        else:
            su += 1
    a.append([aa, su])
    return a


def jo(x):  # listをスペースごとに分ける
    return " ".join(map(str, x))


def max2(x):  # 他のときもどうように作成可能
    return max(list(map(max, x)))


def In(x, a):  # aがリスト(sorted)
    k = bs.bisect_left(a, x)
    if k != len(a) and a[k] == x:
        return True
    else:
        return False


n = onem()

p = [0] + l() + [n + 1]
ans = 0
a = [0 for i in range(n + 2)]

for i in range(n + 2):
    a[p[i]] = i

l = [set() for i in range(n + 2)]
r = [set() for i in range(n + 2)]

for i in range(n + 2):
    l[i].add(max(0, i - 1))
    l[i].add(max(0, i - 2))
    r[i].add(min(n + 1, i + 1))
    r[i].add(min(n + 1, i + 2))


for i in range(n + 1):
    m = a[i]
    x2, x1, y1, y2 = min(l[m]), max(l[m]), min(r[m]), max(r[m])
    hoge = i * (abs((m - x1) * (y2 - y1)) + abs((y1 - m) * (x1 - x2)))
    ans += hoge

    r[x1].clear()
    r[x1].add(y1)
    r[x1].add(y2)

    l[y1].clear()
    l[y1].add(x1)
    l[y1].add(x2)

    r[x2].clear()
    r[x2].add(x1)
    r[x2].add(y1)

    l[y2].clear()
    l[y2].add(y1)
    l[y2].add(x1)


print(ans)
