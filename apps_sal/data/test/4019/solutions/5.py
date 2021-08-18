n, m, d = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]

haveOne = [False] * (n + 1)

for i in range(m):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    if u == 1:
        haveOne[v] = True
    if v == 1:
        haveOne[u] = True

count = 0
group = [-1] * (n + 1)
selectedOne = []

for i in range(2, n + 1):
    if group[i] == -1:
        group[i] = count
        useOne = False
        if haveOne[i]:
            selectedOne.append(i)
            useOne = True
        if count >= d:
            count += 1
            break
        incount = count + 1
        qu = []
        qu += g[i]

        while len(qu) > 0:
            c = qu.pop()
            if c != 1 and group[c] == -1:
                if haveOne[c] and not(useOne):
                    selectedOne.append(c)
                    useOne = True
                group[c] = count
                qu += g[c]
        count += 1

if count > d or d > len(g[1]):
    print('NO')
else:
    diffOne = list(set(g[1]) - set(selectedOne))
    diffOne = selectedOne + diffOne
    g[1] = diffOne[:d]
    visited = [False] * (n + 1)
    qVisit = [1]
    visited[1] = True

    print('YES')
    while len(qVisit) > 0:
        i = qVisit.pop()
        for j in g[i]:
            if not(visited[j]):
                print(i, j)
                visited[j] = True
                qVisit.append(j)
