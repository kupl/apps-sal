import sys
from math import factorial
n = int(sys.stdin.readline())
print(factorial(n) % (10 ** 9 + 7))
