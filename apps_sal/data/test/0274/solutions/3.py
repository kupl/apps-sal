n = int(input())
s = input()
d = 0
md = 0
for i in s:
    if i == '[':
        d += 1
    else:
        d -= 1
    md = max(md, d)
nv = md * 2 - 1
out = ''
res = []
i = 0
while i < n:
    out += '+'
    out += '|' * nv
    out += '+'
    res.append(out)
    out = ''
    while i != n - 1 and s[i + 1] == '[':
        nv -= 2
        out += '-'
        out += '+'
        out += '|' * nv
        out += '+'
        out += '-'
        res.append(out)
        out = ''
        i += 1
    out += '-'
    out += ' ' * nv
    out += '-'
    res.append(out)
    out = ''
    res.append(' ' * (nv + 2))
    i += 1
    out += '-'
    out += ' ' * nv
    out += '-'
    res.append(out)
    out = ''
    while i != n - 1 and s[i + 1] == ']':
        out += '-'
        out += '+'
        out += '|' * nv
        out += '+'
        out += '-'
        res.append(out)
        out = ''
        nv += 2
        i += 1
    out += '+'
    out += '|' * nv
    out += '+'
    res.append(out)
    out = ''
    i += 1
norm = md * 2 + 1
for i in range(len(res)):
    if len(res[i]) == norm:
        continue
    else:
        otk = (norm - len(res[i])) // 2
        res[i] = ' ' * otk + res[i] + ' ' * otk
for i in range(norm):
    for j in range(len(res)):
        print(res[j][i], end='')
    print()
'\n8\n[[][]][]\n\n6\n[[[]]]\n\n6\n[[][]]\n\n2\n[]\n\n4\n[][]\n'
