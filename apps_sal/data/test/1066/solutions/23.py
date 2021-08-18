import sys
from math import ceil
my_file = sys.stdin
line = my_file.readline().split()
n, k = int(line[0]), int(line[1])

if n % 2 == 0:
    if k <= n / 2:
        print(k * 2 - 1)
    else:
        print(int((k - n / 2) * 2))
else:
    if k <= ceil(n / 2):
        print(k * 2 - 1)
    else:
        print(int((k - ceil(n / 2)) * 2))
