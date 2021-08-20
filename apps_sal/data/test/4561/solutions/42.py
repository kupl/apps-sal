(x, a, b) = list(map(int, input().split()))
if a >= b:
    print('delicious')
elif b - a < x + 1:
    print('safe')
else:
    print('dangerous')
