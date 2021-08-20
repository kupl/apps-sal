(a, b, x, y) = list(map(int, input().split()))
diff = a - b
if diff == 0:
    print(x)
elif diff > 0:
    print(min(x + (abs(diff) - 1) * y, (abs(diff) * 2 - 1) * x))
else:
    print(min(x + abs(diff) * y, (abs(diff) * 2 + 1) * x))
