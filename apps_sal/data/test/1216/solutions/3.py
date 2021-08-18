

odd = input()
s = input()

res = ""
vows = "aeiouy"
e = "eo"

a = []
pr = '@'
for ch in s:
    if pr == ch:
        a[-1] += ch
    else:
        a.append(str(ch))
    pr = ch
for g in a:
    if len(g) == 1 or len(g) == 2 and g[0] in e or g[0] not in vows:
        res += g
    else:
        res += g[0]
print(res)
