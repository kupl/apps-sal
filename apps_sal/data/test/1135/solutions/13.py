from collections import defaultdict
import sys
import os
import math


def __starting_point():
    n = int(input())
    s = input()
    ans = ""
    if len(s) % 2 == 1:
        ans += s[0]
        s = s[1:]
    for i in range(len(s)):
        if i % 2 == 0:
            ans = s[i] + ans
        else:
            ans = ans + s[i]
    print(ans)


__starting_point()
