from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


vowel = {'a', 'u', 'i', 'e', 'o'}
S = input()
is_vowel = True
for char in S:
    if not is_vowel and char not in vowel:
        print('NO')
        quit()
    if char in vowel or char == 'n':
        is_vowel = True
    else:
        is_vowel = False
if not is_vowel:
    print('NO')
    quit()
print('YES')
