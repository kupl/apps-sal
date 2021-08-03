import os
import sys
import re
import math

(N, A, B) = [int(n) for n in input().split()]

S = A + B
print((N // S * A + min(N % S, A)))
