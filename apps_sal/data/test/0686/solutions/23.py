from sys import *
from heapq import *
for q in range(int(input())):
    (x, y) = map(int, input().split())
    if x > y + 1:
        print('YES')
    else:
        print('NO')
'\n1\n8\n100 200 100 200 100 200 100 100\n10 2\n15 3\n107\n3\n'
