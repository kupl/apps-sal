s = '!' + input()
m = set(s)
d = {}
d1 = {}
for x in range(1, len(s)):
    if not s[x] in d:
        d[s[x]] = x
    else:
        d[s[x]] = max(d[s[x]], x - s[:x].rindex(s[x]))
    d1[s[x]] = x
for (x, y) in list(d.items()):
    d[x] = max(d[x], len(s) - d1[x])
print(min(d.values()))
