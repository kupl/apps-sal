A, B, C = list(map(int, input().split()))
if (-100 <= A and A <= 100) and (-100 <= B and B <= 100) and (-100 <= C and C <= 100):
    if A == B:
        print(C)
    elif B == C:
        print(A)
    elif C == A:
        print(B)
