(r, g, b) = map(int, input().split())
print('YES' if (g * 10 + b) % 4 == 0 else 'NO')
