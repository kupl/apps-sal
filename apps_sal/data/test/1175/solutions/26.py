L, R = map(int, input().split())

mod = 10**9 + 7


def f(L, R):
    if L > R: return 0
    R = bin(R)[2:]
    N = len(R)
    ret = f(L, int("0" + "1" * (N - 1), 2))
    L = bin(L)[2:]
    if len(L) != N: L = "1" + "0" * (N - 1)
    for i in range(N):
        if R[i] == "0": continue
        R2 = R[:i] + "0" + "?" * (N - i - 1)
        if i == 0: R2 = R
        for j in range(N):
            if L[j] == "1" and j != 0: continue
            L2 = L[:j] + "1" + "?" * (N - j - 1)
            if j == 0: L2 = L
            tmp = 1
            for r, l in zip(R2, L2):
                if r == "0" and l == "1": tmp *= 0; break
                elif r == "?" and l == "?": tmp = tmp * 3 % mod
                elif r == "?" and l == "0": tmp = tmp * 2 % mod
                elif r == "1" and l == "?": tmp = tmp * 2 % mod
            ret += tmp
            ret %= mod
    return ret


print(f(L, R))
