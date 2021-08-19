(a, b, c) = list(map(int, input().split()))
if a == b + c or b == a + c or c == a + b:
    print('Yes')
else:
    print('No')
