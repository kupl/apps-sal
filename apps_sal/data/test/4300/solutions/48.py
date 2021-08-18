from itertools import combinations as cmb
import numpy as np

N = int(input())

d = list(map(int, input().split()))

x, y = np.array(list(cmb(d, 2))).T

print(np.sum(x * y))
