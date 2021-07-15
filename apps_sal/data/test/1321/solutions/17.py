n = int(input())
ws, hs, ans = [], [], ''
for i in range(n):
    w,h = map(int,input().split())
    ws.append(w)
    hs.append(h)
const = tuple(hs)
sum_ws = sum(ws)
max_hs = (max(hs), hs.index(max(hs)))
for i in range(n):
    if i == max_hs[1]:
        hs[i] = 0
        ans += str((sum_ws-ws[i])*max(hs)) + ' '
        hs = list(const)
        max_hs = (max(hs), hs.index(max(hs)))
    else:
        ans += str((sum_ws-ws[i])*max_hs[0]) + ' '
print(ans[:-1])
