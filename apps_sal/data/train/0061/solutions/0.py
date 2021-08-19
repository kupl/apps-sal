import sys
import math
import random
input = sys.stdin.readline


def inp():
    return int(input())


def inara():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return list(map(int, input().split()))


t = inp()
for _ in range(t):
    n = inp()
    ara = inara()
    ans = []
    for i in range(1, n - 1):
        if ara[i] > ara[i - 1] and ara[i] > ara[i + 1]:
            ans.append(i)
            ans.append(i + 1)
            ans.append(i + 2)
            break
    if len(ans) == 0:
        print('NO')
    else:
        print('YES')
        print(*ans)
