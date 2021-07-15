import os
import sys

n = int(sys.stdin.readline())

if n % 3 != 2:
    sys.stdout.write("{0} {1} {2}".format(1, 1, n - 2))
else:
    sys.stdout.write("{0} {1} {2}".format(1, 2, n - 3))

