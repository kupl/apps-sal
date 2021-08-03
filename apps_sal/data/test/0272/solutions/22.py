s = input()
s1 = input()
d = dict()
f = True
for i in range(len(s)):
    a = min(s[i], s1[i])
    b = max(s[i], s1[i])
    if a != b:
        if (a in d and d[a] != b) or (b in d and d[b] != a):
            f = False
            break
        else:
            d[a] = b
            d[b] = a
    else:
        if a in d and d[a] != a:
            f = False
            break
        else:
            d[a] = a
if f:
    a = []
    for i in list(d.items()):
        if i[0] < i[1]:
            a.append((i[0], i[1]))
    print(len(a))
    for i in a:
        print(*i)
else:
    print(-1)
