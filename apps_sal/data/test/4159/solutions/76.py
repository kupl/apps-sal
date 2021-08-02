A, B, K = map(int, input().split())

if K < A:
    A = A - K
elif A <= K and K - A < B:
    B = B - (K - A)
    A = 0
else:
    A = 0
    B = 0

print(A, B)
