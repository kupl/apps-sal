from collections import deque
from sys import stdin, stdout  
import math
input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    x = input()
    first = x.count('1')
    second = x.count('0')
    print('DA' if min(first, second) % 2 else 'NET')

