import sys
from math import sqrt

first = True
table = []
at = 0
for line in sys.stdin:
    if first:
        n = int(line)
        first = False
        continue
    table.append([int(a) for a in line.split()])
    at +=1
    if at==n:
        break

at = 0
end = ' '
for i, line in enumerate(table):
    a_i = int(sqrt(line[i-1]*line[i-2]/table[i-1][i-2]))
    at += 1
    if at == n:
        end='\n'
    print(a_i, end=end)

