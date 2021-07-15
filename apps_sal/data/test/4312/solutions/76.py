a, b, c, d = map(int, input().split())

while a > 0 and c > 0:
    a = a - d
    c = c - b

if c <= 0:
    print('Yes')
else:
    print('No')
