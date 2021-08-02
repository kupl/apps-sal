from collections import defaultdict

h, w, n = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
d = defaultdict(int)
L = [0] * 10
L[0] = (h - 2) * (w - 2)
for a, b in AB:
    for i in range(-1, 2):
        for j in range(-1, 2):
            y, x = a + i, b + j
            if 1 < y < h and 1 < x < w:
                d[(y, x)] += 1
                L[d[(y, x)]] += 1
                L[d[(y, x)] - 1] -= 1
print(*L, sep="\n")
