import sys
from collections import namedtuple
from itertools import groupby
input = sys.stdin.readline


def main():
    Data = namedtuple('Data', ['arr', 'l', 'r'])

    _ = int(input())
    a = list(map(int, input().split()))

    f = [[0, 0] for i in range(max(a) + 2)]

    for x in a:
        f[x][0] = x
        f[x][1] += 1

    best = 0
    opt = None

    for k, v in groupby(f, key=lambda x: 1 if x[1] else 0):
        if not k:
            continue

        v = list(v)
        i = lst = len(v) - 1
        t = [0] * (len(v) + 1)

        while i >= 0:
            t[i] = t[i + 1] + v[i][1]

            if t[i] - t[lst + 1] > best:
                best = t[i] - t[lst + 1]
                opt = Data(v, i, lst)

            if v[i][1] == 1:
                lst = i

            i -= 1

    ans = []

    for i in range(opt.l, opt.r + 1):
        ans.append(opt.arr[i][0])
        opt.arr[i][1] -= 1

    for i in range(opt.r, opt.l - 1, -1):
        while opt.arr[i][1]:
            ans.append(opt.arr[i][0])
            opt.arr[i][1] -= 1

    print(len(ans))
    print(" ".join(map(str, ans)))


main()
