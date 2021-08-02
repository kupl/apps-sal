
icase = 0
if icase == 0:
    n = int(input())
    s = input()
elif icase == 1:
    n = 3
    s = "())"
elif icase == 2:
    n = 6
    s = ")))())"
elif icase == 3:
    n = 8
    s = "))))(((("

l = []
r = []
sim = s[0]
if sim == "(":
    lidx = 0
    l.append(1)
    ridx = -1
elif sim == ")":
    lidx = 0
    l.append(0)
    ridx = 0
    r.append(1)

for i in range(1, len(s)):
    if s[i] == "(" and s[i - 1] == "(":
        l[lidx] += 1
    elif s[i] == "(" and s[i - 1] == ")":
        lidx += 1
        l.append(1)
    elif s[i] == ")" and s[i - 1] == ")":
        r[ridx] += 1
    elif s[i] == ")" and s[i - 1] == "(":
        ridx += 1
        r.append(1)

ll = sum(l)
rr = sum(r)
ds = ll - rr

if len(l) > len(r):
    r.append(0)
elif len(l) < len(r):
    l.append(0)
xmin = 100
x = 0
for i in range(len(l)):
    x = x + l[i] - r[i]
    xmin = min(x, xmin)
if xmin > 0:
    xmin = 0

strs = "(" * (-xmin) + s + ")" * (ds - xmin)
print(strs)
