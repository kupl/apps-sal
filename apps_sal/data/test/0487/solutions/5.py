from sys import stdin, stdout
from math import sin, tan, cos
n = int(stdin.readline())
vl = list(map(int, stdin.readline().split()))
for i in range(max(vl), 300):
    if i * n - sum(vl) > sum(vl):
        stdout.write(str(i))
        break
