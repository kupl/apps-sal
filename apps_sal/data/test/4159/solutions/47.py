(A, B, K) = [int(n) for n in input().split()]
if 0 <= K < A:
    (A, B) = (A - K, B)
elif A <= K < A + B:
    (A, B) = (0, A + B - K)
elif A + B <= K:
    (A, B) = (0, 0)
print(A, B)
