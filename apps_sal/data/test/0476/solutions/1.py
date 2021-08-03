#!/usr/bin/env python3
t = input()


def is_magic(s):
    if (len(s) >= 3):
        if s[-3:] == '144':
            return is_magic(s[:-3])
    if (len(s) >= 2):
        if s[-2:] == '14':
            return is_magic(s[:-2])
    if (len(s) >= 1):
        if s[-1:] == '1':
            return is_magic(s[:-1])
    if (len(s) == 0):
        return True
    return False


if is_magic(t):
    print("YES")
else:
    print("NO")
