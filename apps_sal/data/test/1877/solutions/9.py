import sys
import math

#f = open('input/input_2', 'r')
f = sys.stdin

N = int(f.readline())
S = f.readline().strip()

kingdom = 0
x = 0
y = 0
ans = 0
for action in S:
    if x == y and \
        ((kingdom == 1 and action == 'U')
         or (kingdom == 2 and action == 'R')):
        ans += 1

    if action == 'U':
        y += 1
    elif action == 'R':
        x += 1

    if x > y:
        kingdom = 1
    elif x < y:
        kingdom = 2

print(ans)
