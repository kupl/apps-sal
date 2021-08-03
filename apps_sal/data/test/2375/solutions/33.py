x, y = list(map(int, input().split()))
result = abs(x - y)


if result <= 1:
    print("Brown")
else:
    print("Alice")
