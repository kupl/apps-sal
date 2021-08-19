import time
import sys
readline = sys.stdin.readline
t = time.time()
d = {'N': -10 ** 9, 'S': 10 ** 9, 'E': 1, 'W': -1}
for _ in range(int(input())):
    s = readline().rstrip()
    pos = 0
    visited = set()
    dist = 0
    for c in s:
        dest = pos + d[c]
        dist += 1 if (pos, dest) in visited or (dest, pos) in visited else 5
        visited.update(((pos, dest), (dest, pos)))
        pos = dest
    print(dist)
while time.time() - t < 0.9:
    pass
