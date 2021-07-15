from bisect import bisect_right
s = tuple(map(lambda c: ord(c) - ord("a"), input()))
t = tuple(map(lambda c: ord(c) - ord("a"), input()))
S, T = set(s), set(t)
if T & S != T:
    print(-1)
    return
d, l = [[] for _ in range(26)], [0] * 26
for idx, c in enumerate(s):
    d[c].append(idx)
    l[c] += 1
prev = -1
loop = 0
for c in t:
    idx = bisect_right(d[c], prev)
    if idx >= l[c]:
        loop += 1
        prev = d[c][0]
    else:
        prev = d[c][idx]
print((loop) * len(s) + prev + 1)
