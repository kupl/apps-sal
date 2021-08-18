import math
import statistics
a = int(input())
f = list(map(int, input().split()))
f.sort()
tyu = statistics.median(f)
if f[len(f) // 2] == f[len(f) // 2 - 1]:
    print(0)
else:
    print(f[len(f) // 2] - f[len(f) // 2 - 1])
