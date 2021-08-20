import sys
import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('Yes') if fl else print('No')


def ips():
    return input().split()


ceil = math.ceil
gcd = math.gcd
RL = sys.stdin.readline
INF = 10 ** 15


def ceilab(a, b):
    return (a + b - 1) // b


def JK(s1, s2):
    if s1 == 'R':
        if s2 == 'P':
            return s2
        else:
            return s1
    elif s1 == 'S':
        if s2 == 'R':
            return s2
        else:
            return s1
    elif s1 == 'P':
        if s2 == 'S':
            return s2
        else:
            return s1


(N, K) = ma()
S = list(input())
S = S * 2
T = []
for k in range(K):
    T = []
    for i in range(N):
        T.append(JK(S[2 * i], S[2 * i + 1]))
    S = T * 2
print(T[0])
