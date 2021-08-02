# cook your dish here
from sys import stdin, stdout

s = stdin.readline().strip()

v = ['A', 'E', 'I', 'O', 'U']
c1 = 0
c2 = 0
for i in range(len(s) - 2):
    if s[i] in v:
        if s[i + 1] in v and s[i + 2] in v:
            c1 = 1
            break
if len(set(s).difference(v)) >= 5:
    c2 = 5
if c1 == 1 and c2 == 5:
    stdout.write(str('GOOD'))
else:
    stdout.write(str(-1))
