(x, a, b) = map(int, input().split())
d = -1 * a + b
if d <= 0:
    print('delicious')
elif abs(d) <= x:
    print('safe')
else:
    print('dangerous')
