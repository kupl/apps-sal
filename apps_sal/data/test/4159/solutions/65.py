A, B, K = map(int, input().split())

if K >= A + B:
    A = 0
    B = 0
if K < A + B:
    if K < A:
        A -= K
    else:
        B -= K - A
        A = 0

print(A, B)
