n, m = list(map(int, input().split()))
if m == 1:
    print((1, 2))
    return
l1 = 1
l2 = m + 2
f = True
for length in range(m, 0, -1):
    if f:
        print((l1, l1 + length))
        l1 += 1
        f = False
    else:
        print((l2, l2 + length))
        l2 += 1
        f = True

