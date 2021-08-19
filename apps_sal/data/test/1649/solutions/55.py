(A, B, C, D) = map(int, input().split())
if A + B == C + D:
    print('Yes')
elif A + C == B + D:
    print('Yes')
elif A + D == B + C:
    print('Yes')
elif A == B + C + D:
    print('Yes')
elif B == A + C + D:
    print('Yes')
elif C == A + B + D:
    print('Yes')
elif D == A + B + C:
    print('Yes')
else:
    print('No')
