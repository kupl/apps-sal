import math
from sys import stdin
N, X, T = [int(_) for _ in stdin.readline().rstrip().split()]
print(math.ceil(N/X)*T)
