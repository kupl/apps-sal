A = list(map(int, input().split()))
A.sort()

A, B, C, D = A

if A + D == B + C or A + B + C == D or A == B == C == D:
    print('Yes')

else:
    print('No')
