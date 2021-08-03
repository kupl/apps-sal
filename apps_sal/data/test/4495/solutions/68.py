a, b, x = map(int, input().split())
b = b // x
a = (a + x - 1) // x
print(b - a + 1)
