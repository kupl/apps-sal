def dist(a, b):
    return (b - a) % n


n, m = list(map(int, input().split(" ")))

sweets = {i: [] for i in range(n)}
for i in range(m):
    s, t = list(map(int, input().split(" ")))
    sweets[s - 1].append(t - 1)

t = {i: 0 for i in range(n)}

for i in range(n):
    sweets[i] = sorted(sweets[i], key=lambda x: -dist(i, x))
    if len(sweets[i]):
        t[i] = (len(sweets[i]) - 1) * n + dist(i, sweets[i][-1])

result = []
for s in range(n):
    max_dist = 0
    for i in range(n):
        if t[i] and t[i] + dist(s, i) > max_dist:
            max_dist = t[i] + dist(s, i)
    result.append(max_dist)

print(" ".join(map(str, result)))
