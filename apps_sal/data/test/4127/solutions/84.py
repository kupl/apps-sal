from decimal import Decimal
(A, B) = list(map(Decimal, input().split()))
ans = A * B
print(int(ans))
