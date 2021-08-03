A, B = [int(_) for _ in input().split()]


def g(n):
    ans = 0
    v = (n // 4) * 4
    for x in range(v, n + 1):
        ans ^= x
    return ans


va = g(A - 1)
vb = g(B)

print((va ^ vb))
