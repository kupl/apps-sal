n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]
r = n - m + 1
print('Yes' if any([all([a[x // r + y // m][x % r + y % m] == b[y // m][y % m] for y in range(m**2)]) for x in range(r**2)]) else 'No')
