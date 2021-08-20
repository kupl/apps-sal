(x, a, b) = map(int, input().split())
b -= a
if b <= 0:
    print('delicious')
elif b > x:
    print('dangerous')
else:
    print('safe')
