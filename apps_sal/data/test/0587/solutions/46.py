n, k = list(map(int, input().split()))
td = []
for _ in range(n):
    td.append(list(map(int, input().split())))
td.sort(key=lambda x: x[1], reverse=True)
td_core = []
td_sel = []
td_sub = []
cat = [0] * (n + 1)
for i in range(n):
    if i < k and cat[td[i][0]] == 0:
        td_core.append(td[i])
        cat[td[i][0]] = 1
    elif i < k:
        td_sel.append(td[i])
    elif cat[td[i][0]] == 0:
        td_sub.append(td[i])
        cat[td[i][0]] = 1

kiso = sum([x[1] for x in td_core]) + sum([x[1] for x in td_sel])
bns = len(td_core)
ans = kiso + bns**2
td_sel.sort(key=lambda x: x[1])
for i in range(min(len(td_sel), len(td_sub))):
    kiso -= td_sel[i][1]
    kiso += td_sub[i][1]
    bns += 1
    ans = max(ans, kiso + bns**2)
print(ans)
