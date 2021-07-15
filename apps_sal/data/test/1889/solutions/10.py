n, m, q = [int(token) for token in input().split()]

g = []

for _ in range(n):
    row = [int(token) for token in input().split()]
    g.append(row)


def row_score(row):
    max_count = 0
    count = 0
    for item in row:
        if item == 1:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count


row_cache = [row_score(row) for row in g]


def score():
    return max(
        rc for rc in row_cache
    )


for turn in range(q):
    i, j = [int(token) - 1 for token in input().split()]
    g[i][j] = 1 - g[i][j]
    row_cache[i] = row_score(g[i])
    print(score())
