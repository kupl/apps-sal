def isin(a, b, h, w):
    return (h >= a and w >= b) or (h >= b and w >= a)


a, b, h, w, n = map(int, input().split())
c = sorted(list(map(int, input().split())), key=lambda x: -x)

if isin(a, b, h, w):
    print(0)
    return

vis = {h: w}
for i in range(len(c)):
    nc = c[i]
    pairs = []
    for l in vis.keys():
        pair = (l, vis[l] * nc)
        if isin(a, b, pair[0], pair[1]):
            print(i + 1)
            return
        pairs.append(pair)
        if nc * l not in vis or vis[l] > vis[nc * l]:
            pair = (nc * l, vis[l])
            if isin(a, b, pair[0], pair[1]):
                print(i + 1)
                return
            pairs.append(pair)
    for p in pairs:
        vis[p[0]] = p[1]
print(-1)
