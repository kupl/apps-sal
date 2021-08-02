x, a, b = list(map(int, input().split()))
if a >= b:
    print('delicious')
elif x + a >= b:
    print('safe')
else:
    print('dangerous')
