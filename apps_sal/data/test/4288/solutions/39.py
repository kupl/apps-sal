A, B, C = map(int, input().split())

if A == B and B != C:
    print("Yes")
elif B == C and C != A:
    print("Yes")
elif C == A and A != B:
    print("Yes")
else:
    print("No")
