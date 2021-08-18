import sys
import math
input = sys.stdin.readline


def inp():
    return(int(input()))


def inara():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))


t = inp()

for _ in range(t):
    a, b = invr()

    if a < b:
        a, b = b, a

    if a % b:
        print(-1)
        continue

    ans = 0

    a //= b

    while a % 8 == 0:
        a //= 8
        ans += 1
    while a % 4 == 0:
        a //= 4
        ans += 1

    while a % 2 == 0:
        a //= 2
        ans += 1

    if a != 1:
        print(-1)
    else:
        print(ans)
