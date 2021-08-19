(A, B) = map(int, input().split())
if A == B:
    print('Draw')
elif A == 1 or (A > B and B != 1):
    print('Alice')
else:
    print('Bob')
