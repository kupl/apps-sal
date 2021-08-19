from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()
s = input()
mdiff = 4 * 26
target = 'ACTG'
for i in range(n - 3):
    diff = 0
    for j in range(0, 4):
        d = min(abs(ord(target[j]) - ord(s[i + j])), 26 - abs(ord(target[j]) - ord(s[i + j])))
        diff += d
    mdiff = min(mdiff, diff)
print(mdiff)
