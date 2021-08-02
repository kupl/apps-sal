from decimal import Decimal
N = int(input())
A = list(map(int, input().split()))
check = 0
for i in range(N):
    check += Decimal(1 / A[i])
ans = Decimal(1 / check)
print(ans)
