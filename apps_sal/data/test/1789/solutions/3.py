a, b, x, y = list(map(int, input().split()))
diff = a - b
if diff == 0:
    print(x)
elif diff > 0:
    print((min(x + (abs(diff) - 1) * y, (abs(diff) * 2 - 1) * x)))
else:
    print((min(x + (abs(diff)) * y, (abs(diff) * 2 + 1) * x)))
# 4 -> 1
# 4a -> 3b -> 3a -> 2b -> 2a -> 1b
# 4a -> 3b -> 2b -> 1b
# 1 -> 4
# 1a -> 1b -> 2a -> 2b -> 3a -> 3b -> 4a -> 4b
# 1a -> 1b -> 2b -> 3b -> 4b

