"""
@author: Saurav Sihag
"""

from sys import stdin, stdout, setrecursionlimit
def rr(): return input().strip()
def rri(): return int(rr())
def rrm(): return [int(x) for x in rr().split()]


def sol():
    n = rri()
    res = ""
    if n == 1:
        print("8")
        return
    if n == 2:
        print("98")
        return

    z = (n + 4 - 1) // 4
    res = '9' * (n - z) + '8' * z
    print(res)
    return


def main():
    T = rri()
    for t in range(1, T + 1):
        ans = sol()


main()
