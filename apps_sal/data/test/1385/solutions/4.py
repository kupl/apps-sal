ans, t = [], input()
i, j = 0, -1
while i < len(t):
    if t[i] == '"':
        ans += t[j + 1: i].split()
        i += 1
        j = t.find('"', i)
        ans.append(t[i: j])
        i = j
    i += 1
ans += t[j + 1:].split()
for i in ans:
    print('<' + i + '>')
