X, A, B = list(map(int, input().split()))
if A - B >= 0:
    print('delicious')
elif A + X - B >= 0:
    print('safe')
else:
    print('dangerous')
