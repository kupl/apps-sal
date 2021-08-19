(r, g, b) = map(int, input().split())
if min(r, g, b) == 0:
    print(r // 3 + g // 3 + b // 3)
else:
    (r1, g1, b1) = ((r - 1) // 3, (g - 1) // 3, (b - 1) // 3)
    (r, g, b) = (r - r1 * 3, g - g1 * 3, b - b1 * 3)
    val = r1 + g1 + b1
    if min(r, g, b) == 1:
        print(val + max(1, r // 3 + g // 3 + b // 3))
    else:
        print(val + min(r, g, b))
