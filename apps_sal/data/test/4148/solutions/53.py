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


n = ni()
s = input()


def wid(w):
    return ord(w) - ord('A')


def ws(wid):
    return chr(wid + ord('A'))


ans = ''
for i in range(len(s)):
    id = (wid(s[i]) + n) % 26
    ans += ws(id)
print(ans)
