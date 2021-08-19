(A, B, C) = map(int, input().split())
if (A == B or B == C or C == A) and (not A == B == C):
    print('Yes')
else:
    print('No')
