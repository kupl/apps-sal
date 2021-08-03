import sys
import math
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
x, = [int(num) for num in lines.pop(0).split(" ")]
max_base = int(math.sqrt(x))
max = 1
for base in range(2, max_base + 1):
    i = 2
    while True:
        tmp_max = base ** i
        if tmp_max <= x:
            if tmp_max > max:
                max = tmp_max
            i += 1
        else:
            break
print(max)
