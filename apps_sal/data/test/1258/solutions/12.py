n = int(input())
h = {}
for i in range(n - 2):
    x, y, z = map(int, input().split())
    if x not in h:
        h[x] = []
    if y not in h:
        h[y] = []
    if z not in h:
        h[z] = []
    h[x].append(y)
    h[x].append(z)
    h[x] = set(h[x])
    h[x] = list(h[x])
    h[y].append(x)
    h[y].append(z)
    h[y] = set(h[y])
    h[y] = list(h[y])
    h[z].append(x)
    h[z].append(y)
    h[z] = set(h[z])
    h[z] = list(h[z])

single = 0
for i in h:
    if len(h[i]) == 2:
        single = i
        break
ans = []
vis = {}
vis[single] = True
ans.append(single)
first = single

if len(h[h[single][0]]) == 3:
    ans.append(h[single][0])
    vis[h[single][0]] = True
    second = h[single][0]
else:
    ans.append(h[single][1])
    vis[h[single][1]] = True
    second = h[single][1]
for i in range(n - 2):
    a = h[first]
    b = h[second]
    a = set(a)
    b = set(b)
    a = a.intersection(b)
    a = list(a)
    for x in a:
        if x not in vis:
            ans.append(x)
            vis[x] = True
            first = second
            second = x
            break
print(" ".join(map(str, ans)))
