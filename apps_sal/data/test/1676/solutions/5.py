n, b = map(int, input().split())
l = [tuple(map(int, input().split())) for i in range(n)]
ch = [0]
ans = []
bd = [0] * (n + 1)
po = ma = 0
for i in range(n):
    t, d = l[i]
    bd[i] = bd[i - 1]
    ch += [max(ma, t) + d]
    while ch[po] <= t:
        po += 1
    if i - po - (bd[i - 1] - bd[po - 1]) == b:
        bd[i] += 1
        ch[-1] = -1
    if ch[-1] > ma:
        ma = ch[-1]
    ans += [str(ch[-1])]
print(' '.join(ans))
