input()
s = input()

w, maxp = 0, 0
cur = 0
inp = False
for c in s:
    if c.isalpha():
        cur += 1
    elif cur > 0:
        if inp:
            w += 1
        cur = 0
    if c == "(":
        inp = True
    if c == ")":
        inp = False
    if not inp and cur > maxp:
        maxp = cur
print(maxp, w)
