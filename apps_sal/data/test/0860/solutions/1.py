import sys
from pprint import pprint

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split(' ')))

s = [[] for i in range(0, n + 1)]

for i, ai in enumerate(a, start=1):
    s[ai].append(i)

# pprint(s)
i = 0
q = []

while True:
    if len(s[i]) > 0:
        # Greedy: Add as many students to the room as possible.
        q.append(str(s[i][-1]))
        i += 1
    else:
        # Remove a team
        if i < 3:
            break
        s[i - 1].pop()
        s[i - 2].pop()
        s[i - 3].pop()
        i -= 3
if len(q) == n:
    print('Possible')
    print(' '.join(q))
else:
    print('Impossible')
