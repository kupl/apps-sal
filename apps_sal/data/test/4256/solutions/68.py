(A, B, C) = list(map(int, input().split()))
if B >= A * C:
    print(C)
elif B <= A * C:
    print(B // A)
