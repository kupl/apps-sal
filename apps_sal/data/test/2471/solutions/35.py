from collections import defaultdict, Counter

h, w, n = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

d = defaultdict(int)

for a, b in ab:
    for hi in range(a - 2, a + 1):
        for wi in range(b - 2, b + 1):
            if 1 <= hi <= h - 2 and 1 <= wi <= w - 2:
                d[(hi, wi)] += 1

c = Counter(list(d.values()))

print(((h - 2) * (w - 2) - sum(c.values())))

for i in range(1, 10):
    print((c[i]))

