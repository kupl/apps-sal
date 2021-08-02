A, B = list(map(int, input().split(' ')))
x, y, z = list(map(int, input().split(' ')))

y_needed = max(0, x * 2 + y - A)
b_needed = max(0, y + 3 * z - B)

print(y_needed + b_needed)
