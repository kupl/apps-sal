from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial

n, s = map(int, stdin.readline().split())
stdout.write(str((s + n - 1) // n))
