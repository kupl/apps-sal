from sys import stdin
from math import *
line = stdin.readline().rstrip().split()
n = int(line[0])
q = int(line[1])
ceiling = int(n * n)
if ceiling % 2 == 0:
    ceiling //= 2
else:
    ceiling = (ceiling + 1) // 2
for i in range(q):
    numbers = list(map(int, stdin.readline().rstrip().split()))
    x = numbers[0] - 1
    y = numbers[1] - 1
    result = 0
    if (x + y) % 2 == 1:
        result += ceiling
    if n % 2 == 0:
        result += x * (n // 2)
        result += y // 2
    else:
        aux = x * n + y
        result += aux // 2
    print(result + 1)
