import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
import sys
letters = ascii_letters
input = stdin.readline
#print = stdout.write

for i in range(int(input())):
#for i in range(1):
    a, b = list(map(int, input().split()))
    print(abs(a - b) // 10 + (1 if abs(a - b) % 10 != 0 else 0))

