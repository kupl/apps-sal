import sys

f = sys.stdin

n, x = map(int, f.readline().split())

a = abs(sum(map(int, f.readline().strip().split())))

i = 0
while a > 0:
    a -= x
    i += 1

print(i)
