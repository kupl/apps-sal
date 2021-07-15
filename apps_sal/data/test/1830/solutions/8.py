n, m = map(int, input().split())

free_verticals = set(range(1, n+1))
free_horizontals = set(range(1, n+1))


for _ in range(m):
    x, y = map(int, input().split())
    free_verticals.discard(x)
    free_horizontals.discard(y)
    print(len(free_horizontals) * len(free_verticals), end=' ')
print()

