(n, m, k) = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
num = 0
clusters = {}
socks = {}
for i in range(m):
    (l, r) = [int(i) for i in input().split()]
    if l not in socks and r not in socks:
        socks[l] = num
        socks[r] = num
        clusters[num] = [l, r]
        num += 1
    elif l not in socks and r in socks:
        socks[l] = socks[r]
        clusters[socks[r]].append(l)
    elif l in socks and r not in socks:
        socks[r] = socks[l]
        clusters[socks[l]].append(r)
    elif socks[r] != socks[l]:
        clusters[socks[l]] += clusters[socks[r]]
        temp = socks[r]
        for sock in clusters[socks[r]]:
            socks[sock] = socks[l]
        clusters.pop(temp)
to_paint = 0
for i in clusters:
    colors = {}
    ma = 0
    for sock in set(clusters[i]):
        k = c[sock - 1]
        if k in colors:
            colors[k] += 1
        else:
            colors[k] = 1
        if colors[k] > ma:
            ma = colors[k]
    to_paint += len(clusters[i]) - ma
print(to_paint)
