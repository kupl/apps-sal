import re
from collections import defaultdict
P = re.compile('\\((\\d+)\\+(\\d+)\\)/(\\d+)')
m = int(input())
s = defaultdict(int)
xs = []
for _ in range(m):
    (a, b, c) = list(map(int, P.match(input()).groups()))
    x = (a + b) / c
    s[x] += 1
    xs.append(x)
print(' '.join((str(s[x]) for x in xs)))
