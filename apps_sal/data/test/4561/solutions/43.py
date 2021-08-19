(x, a, b) = map(int, input().split())
tmp = b - a
if tmp <= 0:
    print('delicious')
elif tmp <= x:
    print('safe')
else:
    print('dangerous')
