"""
NTC here
"""
import sys
inp = sys.stdin.readline


def input():
    return inp().strip()


def iin():
    return int(input())


def lin():
    return list(map(int, input().split()))


def main():
    T = iin()
    while T:
        T -= 1
        (n, m) = lin()
        a = lin()
        ans = sum(a)
        print(min(ans, m))


main()
'\n1\n5\n1 3\n1 4\n1 6\n2 6\n0 5\n'
