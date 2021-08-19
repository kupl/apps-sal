(r, g, b) = map(int, input().split())
x = 2 * g + b
print('YES' if x % 4 == 0 else 'NO')
