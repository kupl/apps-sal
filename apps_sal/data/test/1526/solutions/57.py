(A, B, C) = sorted(map(int, input().split()))
(a, b) = divmod(2 * C - A - B, 2)
print(a + b * 2)
