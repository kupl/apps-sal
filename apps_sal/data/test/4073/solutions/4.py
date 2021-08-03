import sys

vec = []
for line in sys.stdin:
    vec.extend(line.split())

vec = [int(x) for x in vec[1:]]
a = int(max(vec))
b = int(vec[-1])
print(a ^ b)
