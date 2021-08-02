a, b = map(float, input().split())
if a % 5 == 0:
    if (a + 0.50) <= b:
        b = b - (a + 0.50)
print(b)
