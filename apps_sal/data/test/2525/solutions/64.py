from collections import deque
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
input = sys.stdin.readline
S = list(input().rstrip())
S = deque(S)
input()
rev = 0
for line in readlines():
    q, *query, = line.split()
    if q == '1':
        rev ^= 1
    else:
        f, c = query
        if f == '1':
            if not rev:
                S.appendleft(c)
            else:
                S.append(c)
        else:
            if not rev:
                S.append(c)
            else:
                S.appendleft(c)

print((''.join(S) if not rev else ''.join(S)[::-1]))

