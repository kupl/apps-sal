(a, b) = map(int, input().split())
if abs(a - b) > 0:
    if a + b + abs(a - b) < 17:
        print('Yay!')
    else:
        print(':(')
else:
    print('Yay!')
