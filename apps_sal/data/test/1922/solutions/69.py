A, B = map(int, input().split())

if (A > 1):
    if (B > 1):
        a = (A - 2) * (B - 2)
    elif B == 1:
        a = (A - 2)
    else:
        a = 0
else:
    if B > 1:
        a = (B - 2)
    elif B == 1:
        a = 1
    else:
        a = 0

print(a)
