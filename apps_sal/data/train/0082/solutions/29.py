import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
import sys
letters = ascii_letters
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(*(list(map(int, input().split()))[::-1]))
