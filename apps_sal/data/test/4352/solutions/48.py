(A, B) = list(map(int, input().split()))
if A == 1:
    A += 100
if B == 1:
    B += 100
if A > B:
    print('Alice')
elif A < B:
    print('Bob')
else:
    print('Draw')
