N = input()
a, b = 0, 1
for i in N:
    x = int(i)
    a, b = min(a + x, b + 10 - x), min(a + x + 1, b + 9 - x)
print(a)
