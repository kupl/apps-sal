A = input()
B = input()
if A > B and len(A) == len(B) or len(A) > len(B):
    print('GREATER')
elif A < B and len(A) == len(B) or len(A) < len(B):
    print('LESS')
else:
    print('EQUAL')
