(A, B) = map(lambda x: int(x) if int(x) > 1 else 14, input().split())
if A > B:
    print('Alice')
if A == B:
    print('Draw')
if A < B:
    print('Bob')
