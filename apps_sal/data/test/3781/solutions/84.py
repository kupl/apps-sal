from collections import Counter
import sys
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().rstrip()


def YesNo(b):
    return bool([print('Yes')] if b else print('No'))


def YESNO(b):
    return bool([print('YES')] if b else print('NO'))


def int1(x):
    return int(x) - 1


T = int(input())
for _ in range(T):
    N = int(input())
    a = tuple(map(int, input().split()))
    if N % 2:
        print('Second')
        continue
    c = Counter(a)
    for v in c.values():
        if v % 2:
            print('First')
            break
    else:
        print('Second')
