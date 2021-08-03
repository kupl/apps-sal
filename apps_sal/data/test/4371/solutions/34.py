import sys

s = str(input())
v = 753
dist = sys.maxsize

for i in range(0, len(s) - 2, 1):
    if dist > abs(int(s[i:i + 3]) - v):
        dist = abs(int(s[i:i + 3]) - v)
print(dist)
