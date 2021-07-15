s1 = input()
s2 = input()
n = len(s1)
d = dict()
for i in range(n):
    a = s1[i]
    b = s2[i]
    if b < a:
        a, b = b, a
    if a not in d and b not in d:
        d[a] = b
        d[b] = a
    elif (a in d and b not in d) or (a not in d and b in d):
        print(-1)
        break
    elif d[a] != b or d[b] != a:
        print(-1)
        break
else:
    ans = []
    for i in list(d.items()):
        if i[0] < i[1]:
            ans.append((i[0], i[1]))
    print(len(ans))
    for elem in ans:
        print(*elem)

