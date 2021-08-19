(x, a, b) = list(map(int, input().split()))
day = b - a
if day <= 0:
    print('delicious')
elif day <= x:
    print('safe')
else:
    print('dangerous')
