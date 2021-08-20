(a, b) = map(float, input().split())
if a % 5 == 0:
    if a + 0.5 <= b:
        b = b - (a + 0.5)
print(b)
