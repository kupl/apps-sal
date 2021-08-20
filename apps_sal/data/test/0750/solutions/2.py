from sys import stdin, stdout
from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
(n, k) = map(int, stdin.readline().split())
stdout.write(str((n * 2 + k - 1) // k + (n * 5 + k - 1) // k + (n * 8 + k - 1) // k))
