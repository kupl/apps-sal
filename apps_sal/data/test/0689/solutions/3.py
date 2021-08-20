import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
letters = ascii_letters
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    have = dict()
    can = True
    for i in range(n):
        for g in input().strip():
            if g not in have:
                have[g] = 0
            have[g] += 1
    for i in list(have.items()):
        if i[1] % n:
            can = False
            break
    print('YES' if can else 'NO')
