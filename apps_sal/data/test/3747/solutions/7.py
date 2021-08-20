q = 'Balbsur'
d = dict([[x, 0] for x in q])
s = input().strip()
for x in s:
    if x in q:
        d[x] += 1
m = min(d['u'], d['a']) // 2
for x in d:
    m = min(m, d[x])
print(m)
