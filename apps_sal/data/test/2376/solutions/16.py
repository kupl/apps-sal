N, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(N)]
mw = wv[0][0]
wv.sort(key=lambda x: -x[1])
values = [[] for _ in range(4)]
for w, v in wv:
    values[w-mw].append(v)


def solve(n, w, c):
    if n >= 4 or w >= W or c >= N:
        return 0
    r = 0
    for i in range(len(values[n])+1):
        cw = w + (mw + n) * i
        cc = c + i
        if cw <= W and cc <= N:
            r = max(r, sum(values[n][0:i]) + solve(n+1, cw, cc))
    return r


print((solve(0, 0, 0)))

