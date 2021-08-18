
from sys import stdin

__author__ = 'artyom'

stdin.readline()
p = stdin.readline().strip()
q = stdin.readline().strip()
print('YES' if (p[0] == '>' and p[-1] == '<' and q[0] == '^' and q[-1] == 'v') or
               (p[0] == '<' and p[-1] == '>' and q[0] == 'v' and q[-1] == '^') else 'NO')
