import os
import sys
import re
import math
(N, R) = [int(n) for n in input().split()]
if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))
