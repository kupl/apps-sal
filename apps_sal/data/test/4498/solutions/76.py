(a, b, c, d) = list(map(int, input().split()))
ab = abs(a - b)
bc = abs(b - c)
ca = abs(c - a)
if ca <= d:
    print('Yes')
elif ab <= d and bc <= d:
    print('Yes')
else:
    print('No')
