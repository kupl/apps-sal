(A, B, C) = list(map(int, input().split()))
if A == B != C or A == C != B or A != B == C:
    print('Yes')
else:
    print('No')
