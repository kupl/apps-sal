(a, b, c, d) = sorted(map(int, input().split()))
if a + d == b + c or a + b + c == d:
    print('Yes')
else:
    print('No')
