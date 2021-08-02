X, A, B = map(int, input().split())
if B <= A:
    print('delicious')
elif A < B and B <= A + X:
    print('safe')
else:
    print('dangerous')
