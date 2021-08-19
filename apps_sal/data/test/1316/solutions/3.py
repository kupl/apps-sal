from collections import Counter
(n, k) = list(map(int, input().split()))
s = input()
c = Counter()
p = ''
r = ''
for t in s:
    if t == p:
        r += t
    else:
        r = t
    if len(r) == k:
        c[r] += 1
        r = ''
    p = t
print(c.most_common(1)[0][1] if len(c) > 0 else 0)
