a, b = list(map(int, input().split()))
c = b - (a + 1) // 2
print([2 * b - 1, 2 * c][c > 0])
