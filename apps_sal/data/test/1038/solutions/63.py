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
    ans = 0
    for i in [A, B]:
        if i % 2 == 1:
            if i // 2 % 2 == 1:
                i = 0
            else:
                i = 1
        elif (i - 1) // 2 % 2 == 1:
            i = 0 ^ i
        else:
            i = 1 ^ i
        ans ^= i
    print(ans)
    return


main()
