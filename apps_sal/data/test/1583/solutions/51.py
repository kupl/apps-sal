"""
Created on Wed Sep  9 19:58:50 2020

@author: liang
"""
import math
'\n【三角形の面積の公式】\nS = 1/2 * a * b\n'
(a, b, x) = map(int, input().split())
L = math.sqrt((x / a / b) ** 2 + b ** 2)
if x >= a ** 2 * b / 2:
    ans = math.degrees(math.atan((b - x / a ** 2) / a * 2))
else:
    ans = math.degrees(math.atan(a * b ** 2 / x / 2))
print(ans)
