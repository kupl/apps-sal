import sys

t = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

t_pos = 0
first = None
for i, c in enumerate(s):
    if c == t[t_pos]:
        t_pos += 1
        if t_pos == len(t):
            first = i
            break

t_pos = len(t) - 1
last = None
for i, c in reversed(list(enumerate(s))):
    if c == t[t_pos]:
        t_pos -= 1
        if t_pos == -1:
            last = i
            break

if first == None or last == None or first > last:
    sys.stdout.write('0\n')
else:
    sys.stdout.write(str(last - first) + '\n')

