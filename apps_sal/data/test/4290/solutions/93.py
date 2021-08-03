import os
import sys
import re
import math

(N, M) = [int(n) for n in input().split()]

cn = (N * (N - 1)) // 2
cm = (M * (M - 1)) // 2
print((cn + cm))
