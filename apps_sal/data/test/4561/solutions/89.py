(x, a, b) = list(map(int, input().split()))
if b <= a:
    print('delicious')
elif a < b and abs(a - b) <= x:
    print('safe')
else:
    print('dangerous')
