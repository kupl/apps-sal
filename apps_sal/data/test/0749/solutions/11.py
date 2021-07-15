s = input()

d = dict()

for i in range(len(s)):
    el = s[i]
    try:
        d[el].append(i)
    except KeyError:
        d[el] = [-1, i]

for i in list(d.keys()):
    d[i].append(len(s))

a = list()
for i in list(d.keys()):
    t = [d[i][j] - d[i][j - 1] for j in range(1, len(d[i]))]
    a.append(max(t))


print(min(min(a), (len(s) + 2) // 2))

