(A, B, C, K) = list(map(int, input().split()))
(a, c) = (min(A, K), max(0, min(C, K - A - B)))
print(a - c)
