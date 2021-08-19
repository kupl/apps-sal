(A, B, C, D, E, F) = map(int, input().split())
ws = set()
for a in range(0, F + 1, 100 * A):
    for b in range(0, F + 1, 100 * B):
        if a + b > F:
            break
        ws.add(a + b)
ws.remove(0)
ss = set()
for c in range(0, F + 1, C):
    for d in range(0, F + 1, D):
        if c + d > F:
            break
        ss.add(c + d)
best_s = -1
best_w = 1
for w in ws:
    for s in ss:
        if w + s > F:
            continue
        if E * w < s * 100:
            continue
        if best_s * (s + w) < s * (best_s + best_w):
            best_s = s
            best_w = w
print(best_s + best_w, best_s)
