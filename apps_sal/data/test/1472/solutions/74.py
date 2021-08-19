(n, x, y) = list(map(int, input().split()))
dists = [0] * (n - 1)
for start in range(n):
    for end in range(start + 1, n):
        dist = min(end - start, abs(x - 1 - start) + 1 + abs(end - (y - 1)))
        dists[dist - 1] += 1
for dist in dists:
    print(dist)
