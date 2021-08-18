import sys
import copy
import math
import itertools
import numpy as np
S = input()
for i in range(1, len(S)):
    l = len(S[0:len(S) - i])
    if l % 2 == 0:
        if S[0:len(S) - i] == S[0:int(l / 2)] + S[0:int(l / 2)]:
            print(l)
            return
