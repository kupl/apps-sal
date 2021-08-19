def calc(n):
    if n == 0:
        return 0
    k = n.bit_length()
    a = k // 2
    b = k - 1 - a
    c = n - 2 ** (k - 1) + 1
    aa = (4 ** a - 1) // 3
    bb = 2 * (4 ** b - 1) // 3
    if k % 2 == 0:
        bb += c
    else:
        aa += c
    aaa = aa ** 2
    bbb = bb * (bb + 1)
    return aaa + bbb


(l, r) = list(map(int, input().split()))
print((calc(r) - calc(l - 1)) % (10 ** 9 + 7))
