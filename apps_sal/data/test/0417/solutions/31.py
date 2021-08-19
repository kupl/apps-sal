def gcd(a: int, b: int) -> int:
    (a, b) = (abs(a), abs(b))
    if a < b:
        (a, b) = (b, a)
    return gcd(b, a % b) if b else a


def sum_seq1(l: int, r: int) -> int:
    if r < l:
        return 0
    return r * (r + 1) // 2 - l * (l - 1) // 2


def sum_difference(N: int, X: int, D: int) -> int:
    if D == 0:
        if X == 0:
            return 1
        return N + 1
    g = gcd(X, D)
    (a, b) = (D // g, -X // g)
    if a < 0:
        a *= -1
        b *= -1
    i_range = [(float('inf'), -float('inf'))] * (N + 1)
    ans = 0
    for k in range(N + 1):
        (kl, kr) = i_range[k]
        nl = sum_seq1(0, k - 1)
        nr = sum_seq1(N - k, N - 1)
        if k + a <= N:
            i_range[k + a] = (b + min(kl, nl), b + max(kr, nr))
        if kr == -float('inf'):
            ans += nr - nl + 1
        elif kr < nl or nr < kl:
            ans += nr - nl + 1
        elif nl <= kl and kr <= nr:
            ans += nr - nl + 1 - (kr - kl + 1)
        elif kl <= nl:
            ans += max(0, nr - kr)
        else:
            ans += kl - nl
    return ans


def __starting_point():
    (N, X, D) = list(map(int, input().split()))
    ans = sum_difference(N, X, D)
    print(ans)


__starting_point()
