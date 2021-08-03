import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input().rstrip()
    n = len(S)

    res1 = res2 = 0
    for i in range(n):
        if i % 2 == 0:
            if S[i] == "0":
                res1 += 1
            else:
                res2 += 1
        else:
            if S[i] == "1":
                res1 += 1
            else:
                res2 += 1
    print((min(res1, res2)))


def __starting_point():
    resolve()


__starting_point()
