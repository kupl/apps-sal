n = int(input())
a, b = 0, n
while a < b - 1:
    c = (a + b) // 2
    if c * (c + 1) // 2 < n:
        a = c
    else:
        b = c
print(n - a * (a + 1) // 2)
