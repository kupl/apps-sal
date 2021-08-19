import math
import collections


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


s = input()
cnt = 0
for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
        cnt += 1
print(cnt)
