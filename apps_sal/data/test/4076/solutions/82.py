"""
Created on Sun Sep  6 12:21:24 2020

@author: liang
"""
import math
pi = 3.141592653589793
(h, m, H, M) = map(int, input().split())
print(math.sqrt(h ** 2 + m ** 2 - 2 * h * m * math.cos(2 * pi * (30 * H - 5.5 * M) / 360)))
