(x, a, b) = map(int, input().split())
if 1 <= b - a <= x:
    print('safe')
elif b - a > x:
    print('dangerous')
else:
    print('delicious')
