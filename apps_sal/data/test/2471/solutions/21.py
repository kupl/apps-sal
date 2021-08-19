from collections import defaultdict, Counter
(h, w, n) = map(int, input().split())
ans = [0] * 10
d = defaultdict(int)
for i in range(n):
    (a, b) = map(int, input().split())
    for j in range(max(2, a - 1), min(a + 2, h)):
        for k in range(max(2, b - 1), min(b + 2, w)):
            d[j, k] += 1
c = Counter(d.values())
print((h - 2) * (w - 2) - sum(c.values()))
for i in range(1, 10):
    print(c[i])
