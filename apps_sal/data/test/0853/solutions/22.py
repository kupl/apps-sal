import os
import sys
import math
fin = sys.stdin
if os.path.exists('in.txt'):
    fin = open('in.txt')
n = int(fin.readline().split()[0])
x = [int(i) for i in fin.readline().split()]
c0 = len([i for i in x if i == 0])
c5 = len([i for i in x if i == 5])
c5 = int(c5 / 9) * 9
if c0 == 0:
    print(-1)
elif c5 == 0:
    print(0)
else:
    s = ''
    for i in range(c5):
        s += '5'
    for i in range(c0):
        s += '0'
    print(s)
