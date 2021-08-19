(s1, s2) = (input(), input())
n = len(s1)
d = dict()
for i in range(n):
    a = s1[i]
    b = s2[i]
    if b < a:
        (a, b) = (b, a)
    if a not in d and b not in d:
        d[a] = b
        d[b] = a
    elif a in d and b not in d or (a not in d and b in d):
        print(-1)
        break
    elif d[a] != b or d[b] != a:
        print(-1)
        break
else:
    k = []
    for i in d.items():
        if i[0] < i[1]:
            k.append('{} {}'.format(i[0], i[1]))
    print(len(k))
    print(*k, sep='\n')
