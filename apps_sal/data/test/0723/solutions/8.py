n = int(input())

hs = []
ws = []
for i in range(n):
    w, h = list(map(int, input().split()))
    hs.append(h)
    ws.append(w)

ans = float('inf')

for H in range(1, 1001):
    wr = 0
    pos = True
    for j in range(n):
        a = min(hs[j], ws[j])
        b = max(hs[j], ws[j])
        if b <= H:
            wr += a
        elif a <= H:
            wr += b
        else:
            pos = False
            break
    if not pos:
        continue
    r = H * wr
    if r < ans:
        ans = r

print(ans)

