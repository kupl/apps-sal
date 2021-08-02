import sys
from math import *
sys.setrecursionlimit(100000000)
n = int(input())
nb = 0
for i in range(2, n):
    nb += n - i
    nb += i - 1
    nb -= 1
print(nb)
