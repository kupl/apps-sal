(n, r) = map(int, input().split())
pt = []
nt = []
r2 = r
result = 0
for _ in range(n):
    (a, b) = map(int, input().split())
    r2 += b
    if b >= 0:
        pt.append((a, b))
    else:
        nt.append((a, b))
pt.sort()
nt.sort(key=lambda t: t[1] + t[0], reverse=True)
for (a, b) in pt:
    if r < a:
        break
    result += 1
    r += b
k = len(nt)
ws = [[0] * (k + 1) for i in range(r + 1)]
for i in range(1, k + 1):
    for w in range(1, r + 1):
        (a, b) = nt[i - 1]
        if w + b >= 0 and a <= r and (ws[r - a][i - 1] >= ws[w][i - 1]):
            ws[w][i] = max(ws[w][i - 1], 1 + ws[w + b][i - 1])
        else:
            ws[w][i] = ws[w][i - 1]
result += ws[r][k]
"\nprint(*enumerate(nt))\nprint(r, k)\nprint(*enumerate(ws), sep='\n')\n"
print(result)
