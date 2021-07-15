a, b, c, d = map(int, input().split())

if d >= abs(a - c) or (d >= abs(a - b) and d >= abs(b - c)):
    print('Yes')
else:
    print('No')
