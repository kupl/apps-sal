x, a, b = map(int, input().split())
if b <= a:
    print('delicious')
elif a < b <= x + a:
    print('safe')
else:
    print('dangerous')
