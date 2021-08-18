"""
NTC here
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))


def main():
    n, c = lin()
    s = lin()
    e = lin()
    sol = [[0, 0] for i in range(n)]
    sol[0] = [c + e[0], s[0]]
    for i in range(1, n - 1):
        sol[i] = [e[i] + min(sol[i - 1][0], c + sol[i - 1][1]), min(sol[i - 1][0], sol[i - 1][1]) + s[i]]
    ans = [0] + [min(sol[i]) for i in range(n - 1)]
    print(*ans)


main()
