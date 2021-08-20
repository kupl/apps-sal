(a, b, c, d) = map(int, input().split())
if abs(b - a) <= d and abs(c - b) <= d:
    print('Yes')
elif abs(c - a) <= d:
    print('Yes')
else:
    print('No')
