import numpy as np
n = int(input())
a = list(map(int, input().split()))
a = [a[i] - i for i in range(n)]
a = np.array(a)
x = np.median(a)
r = 0
for i in range(n):
    r += abs(a[i] - x)
print(int(r))
