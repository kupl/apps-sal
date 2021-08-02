import sys
import string
from decimal import *
from itertools import *
from math import *


def solve():
    p, n = list(map(int, input().split()))
    x = []
    for i in range(n):
        val = int(input())
        if (val % p) not in x:
            x.append(val % p)
        else:
            print(i + 1)
            return 0
    print(-1)


solve();
