n, s = int(input()), input()
d, o, z = dict([((0, 0), -1)]), 0, 0
ans = 0
for i in range(len(s)):
    o += int(s[i] == '1')
    z += int(s[i] == '0')
    tp = (o - min(o, z), z - min(o, z))
    if tp in list(d.keys()):
        ans = max(ans, i - d[tp])
    else:
        d[tp] = i
print(ans)
