# -*- coding: utf-8 -*-

import sys
import os
import math

# input_text_path = __file__.replace('.py', '.txt')
# fd = os.open(input_text_path, os.O_RDONLY)
# os.dup2(fd, sys.stdin.fileno())

n = int(input())

if n < 10:
    print(1)
else:
    s = str(n)
    l = len(s)

    v = 10 ** (l-1)
    w = int(s[1:])

    print(v - w)
