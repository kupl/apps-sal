(a, b) = map(int, input().split())
mat = [['.'] * 50 + ['#'] * 50 for _ in range(100)]
for i in range(a - 1):
    c = 51 + 2 * (i % 24)
    d = 1 + 2 * (i // 24)
    mat[d][c] = '.'
for i in range(b - 1):
    c = 1 + 2 * (i % 24)
    d = 1 + 2 * (i // 24)
    mat[d][c] = '#'
print(100, 100)
for x in mat:
    print(*x, sep='')
