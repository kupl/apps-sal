import math
from collections import Counter
from itertools import product

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

a = input()
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(len(day)):
    if day[i] == a:
        print(7 - i)
