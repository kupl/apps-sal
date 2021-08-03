# 054_a
A, B = list(map(int, input().split()))
if (1 <= A & A <= 13) & (1 <= B & B <= 13):
    if A == B:
        print('Draw')
    elif A == 1:
        print('Alice')
    elif B == 1:
        print('Bob')
    elif A > B:
        print('Alice')
    elif A < B:
        print('Bob')
