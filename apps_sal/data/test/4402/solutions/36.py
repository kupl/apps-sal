(a, b) = map(int, input().split())
if a >= 13:
    print(b)
elif a >= 6 and a <= 12:
    print(b // 2)
elif a <= 5:
    print('0')
