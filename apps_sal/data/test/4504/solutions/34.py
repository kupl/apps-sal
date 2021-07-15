#!/usr/bin/env python3
S = input()

n = 0
for i in range(200):
    n += 2
    s = S[:len(S) - n]

    if s[: len(s) // 2] == s[len(s) // 2:]:
        print((len(s)))
        return

