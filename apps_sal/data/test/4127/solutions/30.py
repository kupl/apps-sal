# C
from decimal import Decimal
A, B = map(Decimal, input().split())
ans = A * B

print(int(ans))
