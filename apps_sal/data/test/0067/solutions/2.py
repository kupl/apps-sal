(a, b, c) = map(int, input().split())
if c == 0:
    if a - b == 0:
        print(0)
    elif a > b:
        print('+')
    else:
        print('-')
elif a - b - c <= 0 and a - b + c >= 0:
    print('?')
elif a - b >= 0:
    print('+')
else:
    print('-')
