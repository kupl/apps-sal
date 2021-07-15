# from sys import stdin
# import math
# import numpy as np
# from itertools import permutations, combinations, combinations_with_replacement

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

a.sort()
suma = sum(a)

for i in range(m):
    print(suma - a[-q[i]])
