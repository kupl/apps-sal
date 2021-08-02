x, y = list(map(int, input().split()))

if x == 0 and y == 1:
    print('Yes')
elif y < 2 or x < 1 or x < (y - 1):
    print('No')
else:
    print('Yes' if (x - (y - 1)) % 2 == 0 else 'No')
