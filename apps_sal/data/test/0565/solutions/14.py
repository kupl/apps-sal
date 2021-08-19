from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
from random import randint
(a, b, c) = map(int, stdin.readline().split())
ans = 0
for i in range(1, a + 1):
    if i + 1 <= b and i + 2 <= c:
        ans = i * 3 + 3
stdout.write(str(ans))
