def S1(r, T, M):
    if r == 1:
        return T % M
    x = pow(r, T, M * (r - 1)) - 1
    return (x // (r - 1)) % M


def S2(r, T, M):
    if r == 1:
        x = T * (T - 1) // 2
        return x % M
    Mr = M * (r - 1)
    x = (T - 1) * pow(r, T, Mr)
    x -= S1(r, T, Mr)
    x += 1
    x //= (r - 1)
    return x


def S(A, B, L, M):
    result = 0
    d = len(str(A))
    start = A
    r = 10**d
    while True:
        n1 = ((r - 1) - A) // B + 1
        items = min(n1, L)
        last = A + (items - 1) * B
        x = last * S1(r, items, M)
        x -= B * S2(r, items, M)
        result *= pow(r, items, M)
        result += x
        result %= M
        r *= 10
        d += 1
        L -= items
        A += B * items
        if L <= 0:
            break
    return result % M


L, A, B, M = map(int, input().split())
answer = S(A, B, L, M)
print(answer)
