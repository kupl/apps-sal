from copy import deepcopy
import itertools
from bisect import bisect_left
import math


def read():
    return int(input())


def readmap():
    return list(map(int, input().split()))


def readlist():
    return list(map(int, input().split()))


N = read()
string_list = []
for _ in range(N):
    s = input()
    string_list.append((len(s), s))

string_list.sort(key=lambda x: x[0])


def is_substring(a, b):  # a is shorter than b
    l_a = len(a)
    l_b = len(b)

    for i in range(l_b - l_a + 1):
        if a == b[i:i+l_a]:
            return True

    return False


for n in range(1, N):
    if not is_substring(string_list[n-1][1], string_list[n][1]):
        print("NO")
        quit()

print("YES")
for n in range(N):
    print(string_list[n][1])

