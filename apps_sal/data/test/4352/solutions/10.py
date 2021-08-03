A, B = list(map(int, input().split()))

if A == 1 and B == 1:
    print('Draw')
elif A == 1 and B != 1:
    print('Alice')
elif B == 1 and A != 1:
    print('Bob')
elif A > B:
    print('Alice')
elif B > A:
    print('Bob')
else:
    print('Draw')
