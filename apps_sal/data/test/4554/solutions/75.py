(W, a, b) = map(int, input().split())
if a > b:
    if a <= b + W:
        print('0')
    else:
        print(a - b - W)
elif b > a:
    if b <= a + W:
        print('0')
    else:
        print(b - a - W)
else:
    print('0')
