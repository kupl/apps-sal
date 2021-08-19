from itertools import combinations as cmbs
import sys
c = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(int(input())):
    si = sys.stdin.readline()[0]
    if si in c:
        c[si] += 1
ans = sum((i * j * k for (i, j, k) in cmbs(list(c.values()), r=3)))
print(ans)
