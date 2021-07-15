from sys import stdin, stdout
from math import factorial
from math import log10

n = int(stdin.readline())
s = set()

q = stdin.readline().strip().split()

for i in range(n):
    f = ''.join(sorted(list(set(list(q[i])))))
    s.add(f)

stdout.write(str(len(s)))
