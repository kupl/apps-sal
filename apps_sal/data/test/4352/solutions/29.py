A, B = list(map(int, input().split()))

if A > B and B != 1:
    print('Alice')

elif A > B and B == 1:
    print('Bob')

elif A < B and A != 1:
    print('Bob')
elif A < B and A == 1:
    print('Alice')
else:
    print('Draw')

