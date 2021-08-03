a, b, c, d = map(int, input().split())
if abs(c - a) <= d:
    print('Yes')
else:
    if abs(a - b) <= d and abs(b - c) <= d:
        print('Yes')
    else:
        print('No')
