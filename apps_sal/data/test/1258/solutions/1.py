from collections import defaultdict
n = int(input())
nei = defaultdict(list)
q = []
for i in range(n - 2):
    (a, b, c) = map(lambda x: int(x) - 1, input().split())
    q.append((a, b, c))
    nei[tuple(sorted((a, b)))].append(c)
    nei[tuple(sorted((a, c)))].append(b)
    nei[tuple(sorted((b, c)))].append(a)
counts = [0] * n
for (a, b, c) in q:
    counts[a] += 1
    counts[b] += 1
    counts[c] += 1
start = next(filter(lambda i: counts[i] == 1, range(n)))
for abc in q:
    if start in abc:
        break
(a, b, c) = abc
if b == start:
    (a, b) = (b, a)
elif c == start:
    (a, c) = (c, a)
if counts[b] != 2:
    (b, c) = (c, b)
p = [a, b, c]
while len(p) < n:
    candidates = nei[tuple(sorted((p[-2], p[-1])))]
    ne = candidates[0]
    if candidates[0] == p[-3]:
        ne = candidates[1]
    p.append(ne)
print(*[x + 1 for x in p])
