# -*- coding: utf-8 -*-

s1, s2 = input().split('^')
s1 = s1[::-1]

l1 = sum([(i + 1) * int(s1[i]) for i in range(len(s1)) if s1[i] != '='])
l2 = sum([(i + 1) * int(s2[i]) for i in range(len(s2)) if s2[i] != '='])

print('balance' if l1 == l2 else 'left' if l1 > l2 else 'right')
