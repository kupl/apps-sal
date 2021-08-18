from functools import lru_cache
from sys import stdin, stdout
import sys
from math import *

input = stdin.readline

for __ in range(int(input())):
    n, m = list(map(int, input().split()))
    ans = "NO"
    for i in range(n):
        a, b = list(map(int, input().split()))
        x, y = list(map(int, input().split()))
        if(x == b):
            ans = "YES"
    if(m % 2 == 1):
        print("NO")
    else:
        print(ans)
