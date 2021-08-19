import collections
import sys
m = collections.defaultdict(int)
line = input()
for d in line.split():
    m[d] += 1
if m['5'] == 2 and m['7'] == 1:
    print('YES')
else:
    print('NO')
