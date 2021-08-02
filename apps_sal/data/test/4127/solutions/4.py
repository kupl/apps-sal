from decimal import Decimal

A, B = list(map(Decimal, input().split()))

A_ = int(A)
B_ = (B * 100)

print((int(A_ * B_ / 100)))
