import sys
line = sys.stdin.readline()[:-1]
a = line.split('+')
a.sort()
print('+'.join(a))
