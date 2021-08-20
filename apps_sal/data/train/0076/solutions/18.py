from sys import stdin, stdout
import math
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print('YES' if n % 4 == 0 else 'NO')
