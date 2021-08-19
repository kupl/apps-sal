def LI():
    return list(map(int, input().split()))


(N, A, B) = LI()
V = LI()
MAX = 51
finv = [None] * MAX


def comb_init():
    finv[0] = 1
    for i in range(1, MAX):
        finv[i] = finv[i - 1] * i


def comb(n, k):
    return finv[n] // finv[k] // finv[n - k]


def main():
    comb_init()
    V.sort(reverse=True)
    s = sum(V[:A])
    mx = s // A if s % A == 0 else s / A
    print(mx)
    if A == N or V[A - 1] > V[A]:
        print(1)
        return
    x = V.count(V[A])
    ans = 0
    if mx == V[A]:
        for i in range(A, B + 1):
            ans += comb(x, i)
    else:
        y = V[:A].count(V[A])
        ans = comb(x, y)
    print(ans)


def __starting_point():
    main()


__starting_point()
