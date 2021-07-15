a, b = map(int, input().split())
if a < b:
    print((a + b - 1) // 2, 1 - (a + b) % 2, 6 - (a + b - 1) // 2 - 1 + (a + b) % 2)
elif a > b:
    print(6 - (a + b - 1) // 2 - 1 + (a + b) % 2, 1 - (a + b) % 2, (a + b - 1) // 2)
else:
    print(0, 6, 0)
