(a, b, x, y) = list(map(int, input().split()))
if b > a:
    use_x = x + 2 * x * (b - a)
    use_y = x + y * (b - a)
elif a == b:
    use_x = x
    use_y = x + y
else:
    use_x = x + 2 * x * (a - b - 1)
    use_y = x + y * (a - b - 1)
print(min(use_x, use_y))
