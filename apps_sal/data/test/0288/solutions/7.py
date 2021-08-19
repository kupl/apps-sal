from sys import stdin
from sys import stdout
n = int(stdin.readline().strip())
m = 1
a = 1
b = 2
while b < n:
    m += 1
    (a, b) = (b, a + b)
if b > n:
    m -= 1
stdout.write(str(m))
