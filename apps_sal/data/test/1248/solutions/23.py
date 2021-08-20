import copy
import sys
line = input()
v = [int(x) for x in line.split()]
resp = 2 * v[0] + 2 * v[1]
resp = min(resp, 2 * v[0] + 2 * v[2])
resp = min(resp, 2 * v[1] + 2 * v[2])
resp = min(resp, v[0] + v[1] + v[2])
print(resp)
