A, B, C, D = list(map(int, input().split()))

bottom = max(A, C)
top = min(B, D)

if top - bottom > 0:
    print((top - bottom))
else:
    print((0))

