def xor_from_zero(to):
    fr = 0
    to_copy = to
    b = 2 ** (len(format(to, 'b')) - 1)
    while b > 2:
        if to_copy // b > 0:
            fr += b
            to_copy -= b
        b = b // 2
    res = 0
    for a in range(fr, to + 1):
        res = res ^ a
    return res


(A, B) = map(int, input().split())
print(xor_from_zero(A - 1) ^ xor_from_zero(B))
