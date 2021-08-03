w, a, b = map(int, input().split())
if b >= a + w:
    print(b - a - w)
else:
    if b + w >= a:
        print('0')
    else:
        print(a - b - w)
