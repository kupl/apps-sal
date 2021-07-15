w, a, b = map(int, input().split())
if a <= b:
    if a + w >= b:
        print(0)
    else:
        print(b - a - w)
else:
    if b + w >= a:
        print(0)
    else:
        print(a - b - w)
