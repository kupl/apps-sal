from decimal import Decimal
(A, B, N) = map(int, input().split())
A = Decimal(A)
B = Decimal(B)
i = min(B - 1, N)
print(int(A * i / B) - A * (i // B))
