(x, y) = map(int, input().split())
print(['No', 'Yes'][y % 2 == 0 and 2 * x <= y <= 4 * x])
