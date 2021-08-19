# -*- coding: utf-8 -*-

S = list(input())
S.insert(0, '0')

for i in range(1, len(S), 2):
    print(S[i], end="")

print()
