(a, b, c, d, e, f) = map(int, input().split())
W = set()
S = set()
sa = 0
wsa = a * 100
for i in range(0, f + a * 100, a * 100):
    for j in range(0, f + b * 100, b * 100):
        w = i + j
        if w <= f:
            W.add(w)
        else:
            break
for i in range(0, f // 2 + c, c):
    for j in range(0, f // 2 + d, d):
        s = i + j
        if s <= f // 2:
            S.add(s)
        else:
            break
S.remove(0)
for i in W:
    for j in S:
        if e / (100 + e) >= j / (i + j) > sa / wsa and i + j <= f:
            (sa, wsa) = (j, i + j)
print(wsa, sa)
