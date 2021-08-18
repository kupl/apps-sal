
from sys import stdin
import re

guys = {'polycarp': 1}

res = 1
stdin.readline()
for line in stdin:
    try:
        to, _, fr = [s.strip().lower() for s in line.lstrip().split(' ', 2)]
    except:
        continue
    guys[to] = max(guys[fr] + 1, guys.get(to, 0))
    res = max(guys[to], res)

print(res)
