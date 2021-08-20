(w, a, b) = map(int, input().split())
if b > a:
    if b - w - a > 0:
        print(b - w - a)
    else:
        print(0)
if a > b:
    if a - w - b > 0:
        print(a - w - b)
    else:
        print(0)
if a == b:
    print(0)
