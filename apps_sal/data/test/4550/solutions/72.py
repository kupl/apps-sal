(a, b, c) = list(map(int, input().split()))
ma = max(a, b, c)
rem = a + b + c - ma
if ma == rem:
    print('Yes')
else:
    print('No')
