from math import *

N = int(input())
abcde = [int(input()) for _ in range(5)]
print((ceil(N / min(abcde)) + 4))
