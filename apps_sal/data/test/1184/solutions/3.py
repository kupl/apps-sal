import sys
3


line = sys.stdin.readline()
s = set()
for c in line:
    if 'a' <= c <= 'z':
        s.add(c)
print(len(s))
