
A, B, C = list(map(int, input().split()))

if A == B and A != C:
    print(C)
elif A == C and A != B:
    print(B)
elif B == C and A != C:
    print(A)
