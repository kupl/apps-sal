# -*- coding: utf-8 -*-

import math

n = int(input())
s = input().split()
for i in range(1,len(s)):
    if math.fabs(int(s[i]) - int(s[i-1])) > 1:
        print("NO")
        return

print("YES")
