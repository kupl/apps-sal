A, B = map(int, input().split())

if A == B:
    print('Draw')
elif A > B != 1 or (A < B and A == 1):
    print('Alice')
else:
    print('Bob')
