import sys

line = sys.stdin.readline()
word = line.split()[0]

n = 0
i = 0
e = 0
t = 0

for c in word:
    if c == 'n':
        n += 1
    elif c == 'i':
        i += 1
    elif c == 'e':
        e += 1
    elif c == 't':
        t += 1

N = max(0, (n - 1) // 2)
I = i
E = max(0, e // 3)
T = t

print(min([N, I, E, T]))

# 1502215214848
