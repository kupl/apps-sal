a, b = map(int, input().split())
x = a + b
if x % 2 == 0:
    print(int(x / 2))
else:
    print(int((x + 1) / 2))
