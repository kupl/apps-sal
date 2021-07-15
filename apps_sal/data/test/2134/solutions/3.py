from collections import defaultdict
import sys


n = int(input())
a = [int(val) for val in input().split()]
b = [int(val) for val in input().split()]

groups = defaultdict(lambda: {'count': 0, 'skill': 0})
for i, val in enumerate(a):
    groups[val]['count'] += 1
    groups[val]['skill'] += b[i]

if len(groups) == n:
    print(0)
    return

group = []
output = 0
individuals = []

for val, desc in list(groups.items()):
    if desc['count'] == 1:
        individuals.append((val, desc['skill']))
    else:
        group.append(val)
        output += desc['skill']

for ival, skill in individuals:
    valid = False
    for gval in group:
        if ival | gval == gval:
            valid = True
    if valid:
        output += skill
print(output)
        

