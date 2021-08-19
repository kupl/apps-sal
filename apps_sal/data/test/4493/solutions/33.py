(a, b, c) = [list(map(int, input().split())) for i in range(3)]
print('Yes' if (a[0] - a[1], a[1] - a[2], a[0] - a[1]) == (b[0] - b[1], b[1] - b[2], b[0] - b[1]) == (c[0] - c[1], c[1] - c[2], c[0] - c[1]) else 'No')
