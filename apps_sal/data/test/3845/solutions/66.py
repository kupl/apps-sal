(a, b) = map(int, input().split())
d = [['#' if i < 50 else '.' for _ in range(100)] for i in range(100)]
for i in range(a - 1):
    d[i // 50 * 4][i % 50 * 2] = '.'
for i in range(b - 1):
    d[99 - i // 50 * 2][i % 50 * 2] = '#'
print(100, 100)
for i in range(100):
    print(*d[i], sep='')
