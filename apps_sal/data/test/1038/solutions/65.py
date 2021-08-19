import sys
from operator import itemgetter
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def lmi():
    return list(map(int, input().split()))


def iif(n):
    return [int(input()) for _ in range(n)]


def lmif(n):
    return [list(map(int, input().split())) for _ in range(n)]


def ss():
    return input().split()


def main():
    mod = 1000000007
    (A, B) = mi()
    A -= 1
    if A % 2 == 1:
        if A // 2 % 2 == 1:
            A = 0
        else:
            A = 1
    elif A // 2 % 2 == 0:
        A = 0 ^ A
    else:
        A = 1 ^ A
    if B % 2 == 1:
        if B // 2 % 2 == 1:
            B = 0
        else:
            B = 1
    elif B // 2 % 2 == 0:
        B = 0 ^ B
    else:
        B = 1 ^ B
    print(A ^ B)
    return


main()
