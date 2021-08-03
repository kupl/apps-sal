x, a, b = map(int, input().split())
y = b - a
if y > x:
    print('dangerous')
elif 0 < y <= x:
    print('safe')
elif y <= 0:
    print('delicious')
