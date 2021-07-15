import sys, math
f = list(map(int, input().split()))
f.sort()
print(f[1] - f[0] + f[2] - f[1])
