import itertools
import math
from collections import defaultdict

def input_ints():
    return list(map(int, input().split()))

def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    for i in range(len(s)):
        x = 0
        if s[i] in 'aiueo':
            x += 1
        if t[i] in 'aiueo':
            x += 1
        if x == 1:
            print('No')
            return
    print('Yes')

def __starting_point():
    solve()

__starting_point()
