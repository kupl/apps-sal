from sys import stdout
from random import randint 
from math import *
import re


n, k = list(map(int, input().split()))

def find_min(n, k):
    return 0 if k == 0 or k == n else 1

def find_max(n, k):
    return min(k * 2, n - k)

print(find_min(n, k), find_max(n, k))

