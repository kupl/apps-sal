a, b = map(int, input().split())
d = [1, 1, 2, 6, 4]
if a == 0:
    print(0 if b >= 5 else d[b])
elif b == 0:
    print(1 if a <= 1 else 0)
else:
    f = 1
    x = a + 1
    while x <= b:
        f *= x
        if x % 10 == 0:
            break
        x += 1
    print(f % 10)
