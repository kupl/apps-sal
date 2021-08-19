from collections import defaultdict

N, W = list(map(int, input().split()))
wv = defaultdict(list)
for _ in range(N):
    w, v = list(map(int, input().split()))
    wv[w].append(v)

for k in list(wv.keys()):
    wv[k].sort(reverse=True)

kw = list(wv.keys())
kw.sort()
l = [len(wv[k]) for k in kw]
l = l + (4 - len(l)) * [0]
# print(l)

ans = 0
for i in range(l[0] + 1):
    wi = kw[0] * i
    if W < wi:
        break
    vi = sum(wv[kw[0]][:i])
    if l[1] == 0:
        ans = max(ans, vi)
    for j in range(l[1] + 1):
        if 2 <= len(kw):
            wj = wi + kw[1] * j
            if W < wj:
                break
            vj = vi + sum(wv[kw[1]][:j])
            if l[2] == 0:
                ans = max(ans, vj)
            for k in range(l[2] + 1):
                if 3 <= len(kw):
                    wk = wj + kw[2] * k
                    if W < wk:
                        break
                    vk = vj + sum(wv[kw[2]][:k])
                    if l[3] == 0:
                        ans = max(ans, vk)
                    for m in range(l[3] + 1):
                        if 4 <= len(kw):
                            wm = wk + kw[3] * m
                            if W < wm:
                                break
                            vm = vk + sum(wv[kw[3]][:m])
                            ans = max(ans, vm)
print(ans)
