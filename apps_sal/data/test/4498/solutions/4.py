(a, b, c, d) = map(int, input().split())
if -d <= a - c <= d:
    print('Yes')
elif -d <= a - b <= d and -d <= b - c <= d:
    print('Yes')
else:
    print('No')
