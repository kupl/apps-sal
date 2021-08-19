import os
import sys
import re
import math
(A, B) = [int(n) for n in input().split()]
answer = -1
for i in range(10001):
    a = i * 8 // 100
    b = i * 10 // 100
    if a == A and b == B:
        answer = i
        break
print(answer)
