n, m = map(int, input().strip().split())
l = [[] for i in range(n + 1)]
count = [0 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().strip().split())
    l[a].append(b)
    l[b].append(a)
    count[a] += 1
    count[b] += 1
mx = 0
v = -1
for i in range(n + 1):
    if count[i] > mx:
        mx = count[i]
        v = i
layer = l[v]
used = [False for i in range(n + 1)]
used[v] = True
for i in l[v]:
    print(v, i)
    used[i] = True
while layer != []:
    newlayer = []
    for i in layer:
        for j in l[i]:
            if used[j] == False:
                print(i, j)
                newlayer.append(j)
                used[j] = True
    layer = newlayer
