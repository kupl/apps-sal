from operator import itemgetter
n, k = map(int, input().split())
td = [list(map(int, input().split())) for _ in range(n)]
td.sort(key=itemgetter(1), reverse=True)
ans = 0
kind = 0
flg = [False] * n
sing, comp = [], []
for i in range(n):
    t, d = td[i]
    t -= 1
    if i < k:
        ans += d
        if flg[t]:
            comp.append(d)
        else:
            flg[t] = True
            kind += 1
    else:
        if not flg[t]:
            sing.append(d)
            flg[t] = True
comp = comp[::-1]
cnt = ans
ans += kind**2
# print(comp)
# print(sing)
if len(comp) > len(sing):
    for i in range(len(sing)):
        dc, ds = comp[i], sing[i]
        cnt += ds - dc
        kind += 1
        ans = max(ans, cnt + kind**2)
else:
    for i in range(len(comp)):
        dc, ds = comp[i], sing[i]
        cnt += ds - dc
        kind += 1
        ans = max(ans, cnt + kind**2)
print(ans)
