# Problem: A. Marketing Scheme
# Contest: Codeforces - Educational Codeforces Round 97 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1437/problem/0
# Memory Limit: 256 MB
# Time Limit: 1000 ms
#
# KAPOOR'S

from sys import stdin, stdout


def INI():
    return int(stdin.readline())


def INL():
    return [int(_) for _ in stdin.readline().split()]


def INS():
    return stdin.readline()


def MOD():
    return pow(10, 9) + 7


def OPS(ans):
    stdout.write(str(ans) + "\n")


def OPL(ans):
    [stdout.write(str(_) + " ") for _ in ans]
    stdout.write("\n")


def __starting_point():
    for _ in range(INI()):
        L, R = INL()
        if R // 2 < L:
            OPS("YES")
        else:
            OPS("NO")


__starting_point()
