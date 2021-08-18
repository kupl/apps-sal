import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
import sys
letters = ascii_letters
input = stdin.readline

for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(abs(a - b) // 10 + (1 if abs(a - b) % 10 != 0 else 0))
