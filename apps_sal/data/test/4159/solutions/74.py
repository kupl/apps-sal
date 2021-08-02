A, B, K = map(int, input().split())

if K <= A:
    A -= K
elif A + B >= K > A:
    B -= K - A
    A = 0
else:
    A, B = 0, 0

print(A, B)
