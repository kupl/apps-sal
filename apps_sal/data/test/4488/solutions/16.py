A = input()
B = input()
if len(A) > len(B):
    print('GREATER')
elif len(A) < len(B):
    print('LESS')
elif A > B:
    print('GREATER')
elif A < B:
    print('LESS')
else:
    print('EQUAL')
