import sys
import itertools
count = int(next(sys.stdin))
x = 0
for line in itertools.islice(sys.stdin, count):
    x += 1 if '++' in line else -1
print(x)
