X, A, B = map(int, input().split())

if A >= B:
    print('delicious')
else:
    if X >= B - A:
        print('safe')
    else:
        print('dangerous')
