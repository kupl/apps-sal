import sys
import string
from decimal import *
from itertools import *
from math import *


def solve():
    s = input()
    k = int(input())
    w = list(map(int, input().split()))
    mm = max(w)
    ans = 0
    for i in range(len(s) + k):
        if (i < len(s)):
            ans = ans + w[ord(s[i]) - ord('a')] * (i + 1)
        else:
            ans = ans + mm * (i + 1)
    print(ans)


solve()
