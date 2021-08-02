import sys

x = str(input()).split()
n = int(x[0])
m = int(x[1])

if n == 1:
    print(1)
    return
if n // 2 < m:
    print(m - 1)
else:
    print(m + 1)
