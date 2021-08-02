n = int(input())
projects = {}
root = None

for i in range(n):
    name, v = input().split()
    v = int(v)
    projects[(name, v)] = []
    m = int(input())

    for j in range(m):
        nn, vv = input().split()
        vv = int(vv)
        projects[(name, v)].append((nn, vv))

    if i < n - 1:
        input()

    if not i:
        root = (name, v)

q = set([root, ])
ans = {}

while q:
    temp = {}

    for u in q:
        for v in projects[u]:
            if v[0] not in ans and v[0] != root[0]:
                if v[0] not in temp:
                    temp[v[0]] = v[1]
                else:
                    temp[v[0]] = max(temp[v[0]], v[1])

    ans.update(temp.items())
    q = set(temp.items())

print(len(ans))
print('\n'.join(list(map(lambda x: ' '.join(str(c) for c in x), sorted(list(ans.items()), key=lambda item: item[0])))))
