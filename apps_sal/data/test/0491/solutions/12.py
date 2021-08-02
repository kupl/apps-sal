import sys

s = sys.stdin.readline().strip()

a = int(s[:-1] if len(s) > 1 and s[:-1] != '-' else s)
b = int(s[:-2] + s[-1] if len(s) > 1 else s)
c = int(s)

print(max(a, b, c))
