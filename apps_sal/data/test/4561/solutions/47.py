(X, A, B) = map(int, input().split())
if A >= B:
    print('delicious')
elif A + X < B:
    print('dangerous')
else:
    print('safe')
