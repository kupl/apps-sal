N, W = map(int, input().split())
data = tuple(tuple(map(int, input().split())) for _ in range(N))
table = [dict() for _ in range(N + 1)]
table[0][0] = 0
for n in range(N):
    weight, value = data[n]
    for w, now in table[n].items():
        table[n + 1][w] = max(table[n + 1].get(w, 0), now)
        if w + weight <= W:
            table[n + 1][w + weight] = max(table[n + 1].get(w + weight, 0), now + value)
print(max(table[N].values()))
