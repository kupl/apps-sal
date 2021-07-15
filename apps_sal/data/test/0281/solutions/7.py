a, b = map(int, input().split())
if b - a < 10:
    c = 1
    for i in range(a + 1, b + 1):
        c *= i
    print(c % 10)
else:
    print(0)
