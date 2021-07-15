# -*- coding: utf-8 -*-
import math

N = int(input())

ans = 10
for A in range(1, int(math.sqrt(N)+1)):
    if N % A == 0:
        B = int(N / A)
        tmp = max(len(str(A)), len(str(B)))
        if ans > tmp:
            ans = tmp

print(ans)

