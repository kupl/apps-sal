from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial


n, s = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))

l, r = -1, min(values) + 1
while r - l > 1:
    m = (l + r) >> 1

    cnt = 0
    for v in values:
        cnt += v - m

    if cnt >= s:
        l = m
    else:
        r = m

if l == -1:
    stdout.write('-1\n')
else:
    stdout.write(str(l) + '\n')
