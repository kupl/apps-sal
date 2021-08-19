(A, B, K) = map(int, input().split())
if A >= K:
    a = A - K
    b = B
else:
    a = 0
    b = max(0, B + A - K)
print(a, b)
