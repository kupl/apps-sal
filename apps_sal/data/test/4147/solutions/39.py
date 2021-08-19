# coding: utf-8

# https://atcoder.jp/contests/abc119


def main():
    N, A, B, C = list(map(int, input().split()))
    ls = [None] * N
    for i in range(N):
        ls[i] = int(input())

    abc_mp = []

    def rec(i, a, b, c, mp, ls):
        if i == len(ls):
            if a > 0 and b > 0 and c > 0:
                abc_mp.append([a, b, c, mp - 30])
        else:
            rec(i + 1, a + ls[i], b, c, mp + 10, ls)
            rec(i + 1, a, b + ls[i], c, mp + 10, ls)
            rec(i + 1, a, b, c + ls[i], mp + 10, ls)
            rec(i + 1, a, b, c, mp, ls)

    rec(0, 0, 0, 0, 0, ls)
    a0, b0, c0, mp0 = abc_mp[0]
    ans = mp0 + abs(A - a0) + abs(B - b0) + abs(C - c0)
    for a, b, c, mp in abc_mp:
        cand = mp + abs(A - a) + abs(B - b) + abs(C - c)
        if cand < ans:
            ans = cand

    return ans


print((main()))
