a, b, c, d = map(int, input().split())

if abs(a - c) <= d:
    print('Yes')
elif (a < b and b < c) or (a > b and b > c):
    if abs(a - b) <= d and abs(b - c) <= d:
        print('Yes')
    else:
        print('No')
else:
    print('No')
