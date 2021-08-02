import sys
st = input()
a = 0
b = 0
last = 0
v = []
for s in st:
    if s == "(":
        a += 1
    elif s == ")":
        a -= 1
    elif s == "#":
        a -= 1
        v.append(1)
    if a < 0:
        print(-1)
        return

v[-1] += a
i = 0
a = 0
for s in st:
    if s == "(":
        a += 1
    elif s == ")":
        a -= 1
    elif s == "#":
        a -= v[i]
        i += 1
    if a < 0:
        print(-1)
        return
if a != 0:
    print(-1)
else:
    for vs in v:
        print(vs)
