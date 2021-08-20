(a, b, c) = [int(x) for x in input().split()]
if b >= c:
    print('delicious')
elif c > a + b:
    print('dangerous')
else:
    print('safe')
