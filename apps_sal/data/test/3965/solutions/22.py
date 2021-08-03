#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

N = int(input())
patterns = list(map(int, input().split()))

vowels = []
for n in range(N):
    c = Counter(input())
    vowel_num = sum(c[x] for x in 'aeiouy')
    vowels.append(vowel_num)

if vowels == patterns:
    print('YES')
else:
    print('NO')
