
n, m = list(map(int, input().split()))

columns = set()
rows = set()

results = []
for _ in range(m):
    x, y = list(map(int, input().split()))

    columns.add(x)
    rows.add(y)

    result = n * (n - len(columns)) - (n - len(columns)) * len(rows)
    results.append(result)

print(' '.join(map(str, results)))

