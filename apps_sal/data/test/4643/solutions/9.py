import sys
import time
for line in sys.stdin:
    for i in range(20000000):
        j = i
    vec = line.split()
    val = [str(y) for y in sorted([int(x) for x in vec[1:]])]
    print(' '.join(val))
