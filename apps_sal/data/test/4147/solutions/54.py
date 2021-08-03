N, A, B, C = list(map(int, input().split()))
L = [int(input()) for _ in range(N)]


def rec(itr, a, b, c, mp):
    if itr == N:
        if a == 0 or b == 0 or c == 0:
            return 10 ** 9
        return abs(a - A) + abs(b - B) + abs(c - C) + mp - 30
    res = rec(itr + 1, a, b, c, mp)
    res = min(res, rec(itr + 1, a + L[itr], b, c, mp) + 10)
    res = min(res, rec(itr + 1, a, b + L[itr], c, mp) + 10)
    res = min(res, rec(itr + 1, a, b, c + L[itr], mp) + 10)
    return res


print((rec(0, 0, 0, 0, 0)))
