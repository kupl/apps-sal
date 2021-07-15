#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().rstrip()
    if len(s) % 2 == 0:
        ben_wins = False
        for ch in s[1::2]:
            if int(ch) % 2 == 0:
                ben_wins = True
    else:
        ben_wins = True
        for ch in s[0::2]:
            if int(ch) % 2 == 1:
                ben_wins = False
    
    if ben_wins:
        print(2)
    else:
        print(1)
