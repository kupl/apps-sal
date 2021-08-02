s = input()

cs = {}
ma = {}
keys = 'abcdefghijklmnopqrstuvwxyz'
for c in keys:
    cs[c] = []
    ma[c] = -1

for i in range(len(s)):
    c = s[i]
    cs[c].append(i)

for c in keys:
    if len(cs[c]) > 0:
        ma[c] = max(cs[c][0] + 1, len(s) - cs[c][-1])
    for i in range(1, len(cs[c])):
        if abs(cs[c][i] - cs[c][i - 1]) > ma[c]:
            ma[c] = abs(cs[c][i] - cs[c][i - 1])

mi = 9999999999
for m in list(ma.values()):
    if m != -1 and m < mi:
        mi = m

print(mi)
