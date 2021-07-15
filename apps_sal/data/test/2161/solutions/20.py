n = int(input())
d = dict()
for i in range(n):
    inp = input().split()
    name, cnt = inp[0], int(inp[1])
    d[name] = d.get(name, set())
    d[name].update(inp[2:])
print(len(d))
for k, v in d.items():
    v = list(v)
    for i in range(len(v)):
        for j in range(len(v)):
            if i != j and len(v[i]) <= len(v[j]) and v[j][len(v[j]) - len(v[i]):] == v[i]:
                v[i] = '-'
    l = 0
    for e in v:
        if e != '-':
            l += 1
    print(k, l, end=' ')
    for e in v:
        if e != '-':
            print(e, end=' ')
    print()

