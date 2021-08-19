(a, b, c) = list(map(int, input().split()))
if a + b + c >= 22:
    print('bust')
elif a + b + c <= 21:
    print('win')
