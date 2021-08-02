n = int(input())
a = [int(t) for t in input().split(' ')]

p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]

sums = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        sums.add(p[j] - p[i])

INF = n + 100
best_blocks = []
for s in sums:
    blocks = []
    leftmost_p = 0
    while leftmost_p < INF:
        leftmost_j = INF
        according_i = -1
        for i in range(leftmost_p, n):
            if i >= leftmost_j: break
            for j in range(i + 1, n + 1):
                if j >= leftmost_j: break
                if p[j] - p[i] == s and j < leftmost_j:
                    leftmost_j = j
                    according_i = i

        leftmost_p = leftmost_j
        if leftmost_j < INF:
            blocks.append((according_i + 1, leftmost_j))

    if len(blocks) > len(best_blocks):
        best_blocks = blocks

print(len(best_blocks))
for b in best_blocks:
    print(*b)
