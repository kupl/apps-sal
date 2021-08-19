(x, a, b) = list(map(int, input().split()))
if a >= b:
    print('delicious')
elif a + x >= b:
    print('safe')
else:
    print('dangerous')
