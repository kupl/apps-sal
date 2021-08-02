import sys
import string
read = lambda: list(map(int, sys.stdin.readline().split()))

n, m = read()
s = sys.stdin.readline().strip()
design = {c: c for c in string.ascii_lowercase}
for i in range(m):
    a, b = sys.stdin.readline().split()
    design[a], design[b] = design[b], design[a]
design2 = {b: a for a, b in list(design.items())}
print(''.join(design2[c] for c in s))
