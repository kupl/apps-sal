N = int(input())
S = input()
(r, g, b) = ([], [], [])
for (idx, w) in enumerate(S):
    if w == 'R':
        r.append(idx + 1)
    elif w == 'G':
        g.append(idx + 1)
    elif w == 'B':
        b.append(idx + 1)
if len(r) >= len(b) and len(r) >= len(g):
    (L, M, S) = (r, g, b)
elif len(b) >= len(r) and len(b) >= len(g):
    (L, M, S) = (b, g, r)
elif len(g) >= len(r) and len(g) >= len(b):
    (L, M, S) = (g, r, b)
L = set(L)
ans = len(S) * len(L) * len(M)
for s in S:
    for m in M:
        tmp = sorted([s, m])
        if tmp[0] - (tmp[1] - tmp[0]) in L:
            ans -= 1
        if tmp[1] + (tmp[1] - tmp[0]) in L:
            ans -= 1
        if sum(tmp) / 2 in L:
            ans -= 1
print(ans)
