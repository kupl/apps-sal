INF = float('inf')
N = int(input())
d = {'R': [[], []], 'L': [[], []], 'U': [[], []], 'D': [[], []]}
for i in range(N):
    x, y, f = input().split()
    x = int(x)
    y = int(y)
    d[f][0].append(x)
    d[f][1].append(y)

Ts = []

xM = max(max(d['U'][0] + [-INF]), max(d['D'][0] + [-INF]))
xMr = max(d['R'][0] + [-INF])
xMl = max(d['L'][0] + [-INF])


def xmax(T):
    return max(xM, xMr + T, xMl - T)


Ts += [max(0, xMl - xM), max(0, xM - xMr), max(0, (xMl - xMr) / 2)]

xm = min(min(d['U'][0] + [INF]), min(d['D'][0] + [INF]))
xmr = min(d['R'][0] + [INF])
xml = min(d['L'][0] + [INF])


def xmin(T):
    return min(xm, xmr + T, xml - T)


Ts += [max(0, xml - xm), max(0, xm - xmr), max(0, (xml - xmr) / 2)]

yM = max(max(d['R'][1] + [-INF]), max(d['L'][1] + [-INF]))
yMu = max(d['U'][1] + [-INF])
yMd = max(d['D'][1] + [-INF])


def ymax(T):
    return max(yM, yMu + T, yMd - T)


Ts += [max(0, yMd - yM), max(0, yM - yMu), max(0, (yMd - yMu) / 2)]

ym = min(min(d['R'][1] + [INF]), min(d['L'][1] + [INF]))
ymu = min(d['U'][1] + [INF])
ymd = min(d['D'][1] + [INF])


def ymin(T):
    return min(ym, ymu + T, ymd - T)


Ts += [max(0, ymd - ym), max(0, ym - ymu), max(0, (ymd - ymu) / 2)]

ans = INF

for T in Ts:
    ans = min(ans, (xmax(T) - xmin(T)) * (ymax(T) - ymin(T)))

print(ans)
