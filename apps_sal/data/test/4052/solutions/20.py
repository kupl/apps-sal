n = int(input())
s = list(input())
t = list(input())
(a, b) = (sorted(s), sorted(t))
if a != b:
    print(-1)
else:
    k = 0
    rec = []
    while k < n:
        while s[k] != t[k]:
            f = s[k:].index(t[k]) + k - 1
            rec.append(f + 1)
            (s[f], s[f + 1]) = (s[f + 1], s[f])
        k += 1
    print(len(rec))
    print(' '.join(map(str, rec)))
