(a, b, c, d) = map(int, input().split())
ct = False
if abs(a - c) <= d:
    ct = True
if abs(a - b) <= d and abs(c - b) <= d:
    ct = True
if ct:
    print('Yes')
else:
    print('No')
