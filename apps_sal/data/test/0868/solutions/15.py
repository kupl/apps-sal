import sys

import math


sz=int(input())
if sz==0:
    print(1)
    return

s = str(8 ** ((sz - 1) % 4 + 1))
print(s[len(s)-1])
