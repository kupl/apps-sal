(N, W) = map(int, input().split())
data = tuple((tuple(map(int, input().split())) for _ in range(N)))
d = {0: 0}
for n in range(N):
    (weight, value) = data[n]
    for (w, now) in d.copy().items():
        if w + weight <= W:
            d[w + weight] = max(d.get(w + weight, 0), now + value)
print(max(d.values()))
