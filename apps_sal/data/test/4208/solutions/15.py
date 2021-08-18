l = int(input())
le = input().strip()
ri = input().strip()
la = list(sorted(((y, x) for x, y in enumerate(le)), reverse=True))
lb = list(sorted(((y, x) for x, y in enumerate(ri)), reverse=True))
i, j = 0, 0
res = 0
resp = []
ui, ul = l - 1, l - 1
while i <= ui and j <= ul:
    ai, aa = la[i]
    bi, bb = lb[j]
    if ai == bi or ai == '?' or bi == '?':
        resp.append("{} {}".format(aa + 1, bb + 1))
        i += 1
        j += 1
    elif ai > bi:
        i += 1
        if lb[ul][0] == '?':
            resp.append("{} {}".format(aa + 1, lb[ul][1] + 1))
            ul -= 1
    else:
        j += 1
        if la[ui][0] == '?':
            resp.append("{} {}".format(la[ui][1] + 1, bb + 1))
            ui -= 1

print(len(resp))
for r in resp:
    print(r)
