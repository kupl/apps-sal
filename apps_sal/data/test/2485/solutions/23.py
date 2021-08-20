(h, w, m) = list(map(int, input().split()))
ms = []
hs = [0 for i in range(h)]
ws = [0 for i in range(w)]
for i in range(m):
    (hi, wi) = list(map(int, input().split()))
    ms.append((hi - 1, wi - 1))
    hs[hi - 1] += 1
    ws[wi - 1] += 1
maxh = max(hs)
maxw = max(ws)
cnt_h = sum([hs[i] == maxh for i in range(h)])
cnt_w = sum([ws[i] == maxw for i in range(w)])
cnt = cnt_h * cnt_w
for (x, y) in ms:
    if hs[x] == maxh and ws[y] == maxw:
        cnt -= 1
if cnt <= 0:
    print(maxh + maxw - 1)
else:
    print(maxh + maxw)
