a, b = map(int, input().split())

if (b - a) >= 5:
    print(0)
else:
    s = 1
    for i in range(a + 1, b + 1):
        s = ((i % 10) * s) % 10
    print(s % 10)
