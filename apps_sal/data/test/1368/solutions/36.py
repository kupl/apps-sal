import sys
input = sys.stdin.readline


def main():
    N, A, B = list(map(int, input().split()))
    v = sorted(list(map(int, input().split())), reverse=True)
    use = v[:A]
    print((sum(use) / A))
    fac = [0 for _ in range(N + 1)]
    fac[0], fac[1] = 1, 1

    for i in range(2, N + 1):
        fac[i] = (fac[i - 1] * i)

    x = v.count(v[A - 1])
    y = use.count(use[A - 1])

    if v[0] == v[A - 1]:
        ans = 0
        for i in range(A, min(B, x) + 1):
            ans += fac[x] // (fac[i] * fac[x - i])
        print(ans)
    else:
        ans = fac[x] // (fac[y] * fac[x - y])
        print(ans)


def __starting_point():
    main()


__starting_point()
