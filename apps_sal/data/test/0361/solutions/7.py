import sys
f = sys.stdin

s = f.readline().strip()
SS = 'CODEFORCES'

res = False

for i in range(len(s)):
    for l in range(len(s)):
        if s[:i] + s[(i + l):] == SS:
            res = True
            break


if res:
    print("YES")
else:
    print("NO")
