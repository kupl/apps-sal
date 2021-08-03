from math import tan, pi
t = int(input())
for _ in range(t):
    n = int(input())
    print(1 / tan(pi / (2 * n)))
