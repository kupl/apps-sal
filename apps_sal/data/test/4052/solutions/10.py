import sys

out = list()
valid = True
l = int(sys.stdin.readline())
s = [char for char in sys.stdin.readline()]
t = [char for char in sys.stdin.readline()]
for loop in range(l):
    i = loop
    while i < l and s[i] != t[loop]:
        i += 1
    if s[i] != t[loop]:
        print(-1)
        valid = False
        break
    for loop2 in range(i, loop, -1):
        out.append(loop2)
        x = s[loop2 - 1]
        s[loop2 - 1] = s[loop2]
        s[loop2] = x
if valid:
    print(len(out))
    print(*out)
