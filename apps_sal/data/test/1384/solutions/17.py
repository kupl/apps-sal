from sys import stdout
from random import randint
from math import *
import re


n = int(input())
s = input().replace(' ', '')

ones = s.count("1")
zeros = 0
mx = 0
for c in s:
    zeros += c == '0'
    if zeros + ones > mx:
        mx = zeros + ones
    ones -= c == '1'

print(mx)
