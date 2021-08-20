import math
import statistics
a = int(input())
f = list(map(int, input().split()))
ans = 0
count = 0
for i in range(a):
    if ans + 1 == f[i]:
        ans = f[i]
        count += 1
if count > 0:
    print(len(f) - count)
else:
    print(-1)
