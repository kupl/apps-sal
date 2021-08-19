(A, B) = map(int, input().split())
(A, B) = ((A + 11) % 13, (B + 11) % 13)
if A < B:
    print('Bob')
elif A > B:
    print('Alice')
else:
    print('Draw')
