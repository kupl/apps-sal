from itertools import groupby as gb
n = int(input())
s = input()
g = gb(s)
gl = []
for k, v in g:
    gl.append([k, len(list(v))])
l = len(gl)

if s[0] == 'S':
    if l == 1:
        print(0)
        return
    elif l <= 3:
        print(gl[1][1])
        return
if s[0] == 'G':
    if l <= 2:
        print(gl[0][1])
        return

res = 0
# 1
for i, [k, v] in enumerate(gl):
    if (k, v) == ('S', 1) and i not in (0, l - 1):
        if s[0] == 'S' and l <= 5:
            res = max(res, gl[i - 1][1] + gl[i + 1][1])
        elif s[0] == 'G' and l <= 4:
            res = max(res, gl[i - 1][1] + gl[i + 1][1])
        else:
            res = max(res, gl[i - 1][1] + gl[i + 1][1] + 1)
# 2
for i, [k, v] in enumerate(gl):
    if (k) == ('S') and v > 1:
        if i != 0:
            res = max(res, gl[i - 1][1] + 1)
        if i != l - 1:
            res = max(res, gl[i + 1][1] + 1)
print(res)
