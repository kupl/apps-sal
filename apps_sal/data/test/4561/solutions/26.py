(x, a, b) = list(map(int, input().split()))
d = b - a
if d <= 0:
    print('delicious ')
elif d <= x:
    print('safe')
else:
    print('dangerous')
