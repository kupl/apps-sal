def main():
    (n, k) = list(map(int, input().split()))
    x = list(map(int, input().split()))
    (m, p) = ([], [])
    for i in range(n):
        if x[i] < 0:
            m.append(x[i])
        else:
            p.append(x[i])
    (M, P) = (len(m), len(p))
    ans = float('inf')
    for i in range(min(M + 1, k + 1)):
        t = 0
        if i > 0:
            t += 2 * abs(m[M - i])
        r = k - i
        if r == 0:
            if t // 2 < ans:
                ans = t // 2
        elif r <= P:
            t += p[r - 1]
            if t < ans:
                ans = t
    for i in range(min(P + 1, k + 1)):
        t = 0
        if i > 0:
            t += 2 * p[i - 1]
        r = k - i
        if r == 0:
            if t // 2 < ans:
                ans = t // 2
        elif r <= M:
            t += abs(m[M - r])
            if t < ans:
                ans = t
    print(ans)


def __starting_point():
    main()


__starting_point()
