from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq
sys.setrecursionlimit(100000)

# input functions for me


def rsa(sep=''):
    if sep == '':
        return input().split()
    else:
        return input().split(sep)


def rip(sep=''):
    if sep == '':
        return list(map(int, input().split()))
    else:
        return list(map(int, input().split(sep)))


def ria(sep=''):
    return list(rip(sep))


def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##


def main():
    N = ri()
    P = [N + 1, N + 1] + ria() + [N + 1, N + 1]

    ord = []
    for i in range(2, N + 2):
        ord.append((P[i], i))

    ord = sorted(ord)  # P[i], i , P[i]順でソート

    # ..AsssBssCssDsssE.. のようになっている（Cが自分 A,B,D,E>C，s<C）
    # CからA,B,D,Eのインデクスを知りたいので，Cより小さい区間は連結にして置き，
    # スキップできるように各連結成分の両端に情報を乗せておく
    #  union-findで管理してもいいが，アクセスする場所と回数が限られているので配列で管理できる
    tot = 0
    l = [i for i in range(N + 4)]
    r = [i for i in range(N + 4)]
    used = [False] * (N + 4)
    for v, idx in ord:
        # 左右がusedならマージする
        used[idx] = True
        if used[idx - 1]:
            l[idx] = l[idx - 1]
        if used[idx + 1]:
            r[idx] = r[idx + 1]
        r[l[idx]] = r[idx]
        l[r[idx]] = l[idx]

        l0 = l[idx] - 1
        r0 = r[idx] + 1
        l1 = l0 - 1 if not used[l0 - 1] else (l[l0 - 1] - 1)
        r1 = r0 + 1 if not used[r0 + 1] else (r[r0 + 1] + 1)
        # print(l1,l0,idx,r0,r1)

        if l1 != 0:
            rseg = r0 - idx
            lseg = l0 - l1
            tot += lseg * rseg * v
        if r1 != N + 3:
            rseg = r1 - r0
            lseg = idx - l0
            tot += lseg * rseg * v

    print(tot)


def __starting_point():
    main()


__starting_point()
