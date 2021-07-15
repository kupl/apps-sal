N = int(input())
A = list(map(int, input().split()))
check = 0
from decimal import Decimal
for i in range(N):
  check += Decimal(1/A[i])
ans = Decimal(1/check)
print(ans)
