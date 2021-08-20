s = input()
letters = set(s)
p = dict.fromkeys(letters, [-1, -1])
for (i, c) in enumerate(s):
    u = max(p[c][1], i - p[c][0])
    p[c] = [i, u]
for value in p.values():
    value[1] = max(len(s) - value[0], value[1])
print(min((i[1] for i in p.values() if i[1] != -1)))
