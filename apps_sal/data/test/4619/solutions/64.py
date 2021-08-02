w, h, n = map(int, input().split())
right, left, lower, upper = 0, w, 0, h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        right = max(right, x)
    if a == 2:
        left = min(left, x)
    if a == 3:
        lower = max(lower, y)
    if a == 4:
        upper = min(upper, y)

a = left - right
b = upper - lower

if a <= 0 or b <= 0:
    print(0)
else:
    print(a * b)
