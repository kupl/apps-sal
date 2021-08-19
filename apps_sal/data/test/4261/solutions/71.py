(A, B, C) = list(map(int, input().split()))
water = A - B
answer = C - water
if answer < 0:
    print(0)
else:
    print(answer)
