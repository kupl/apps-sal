n = int(input())
a = list(map(int, input().split()))

ps = a[0]
ans = 0
h = {a[0]: 1}
hv = {a[0]: a[0]}


def gv(h, k):
    if k in h:
        return h[k]
    else:
        return 0


for i in range(1, n):
    c = i - gv(h, a[i]) - gv(h, a[i] - 1) - gv(h, a[i] + 1)
    cps = ps - gv(hv, a[i]) - gv(hv, a[i] - 1) - gv(hv, a[i] + 1)
    ans += a[i] * c - cps
    if a[i] not in h:
        h[a[i]] = 0
        hv[a[i]] = 0
    h[a[i]] += 1
    hv[a[i]] += a[i]
    ps += a[i]
print(ans)
