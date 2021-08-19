import sys
inp = sys.stdin
n = int(inp.readline())
x = 0
for i in range(n):
    s = inp.readline()
    if '-' in s:
        x -= 1
    else:
        x += 1
print(x)
