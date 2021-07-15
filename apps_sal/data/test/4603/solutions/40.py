import sys
A, B, C, D = map(int, sys.stdin.readlines())
import numpy as np
train, bus = np.array([[A,B]]), np.array([[C,D]]).T
print((train+bus).min())
