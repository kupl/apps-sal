s = input()

mode = 0
l = len(s)
r = -1
for i in range(len(s)):
    if mode == 0:
        if s[i] == "[":
            mode = 1
    if mode == 1:
        if s[i] == ":":
            l = i
            break

mode = 0
for i in range(len(s) - 1, -1, -1):
    if mode == 0:
        if s[i] == "]":
            mode = 1
    if mode == 1:
        if s[i] == ":":
            r = i
            break

if l >= r:
    print(-1)
else:
    c = 0
    for i in range(l + 1, r):
        if s[i] == "|":
            c += 1
    print(c + 4)
