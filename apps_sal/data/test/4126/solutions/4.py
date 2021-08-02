import os
import sys
import re
import math

S = input()

s1 = S[:(len(S) - 1) // 2]
s2 = S[(len(S) + 3) // 2 - 1:]
if S[::-1] == S and s1[::-1] == s1 and s2[::-1] == s2:
    print('Yes')
else:
    print('No')
