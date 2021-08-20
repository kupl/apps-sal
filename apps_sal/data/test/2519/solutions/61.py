def main():
    (n, k) = map(int, input().split(' '))
    p = list(map(int, input().split(' ')))
    u = [0]
    v = []
    w = []
    for i in range(n):
        u.append(u[i] + p[i])
    for i in range(n - k + 1):
        w.append(u[k + i] - u[i])
    x = w.index(max(w))
    for i in range(k):
        v.append(p[x + i])
    a = 0
    for i in range(k):
        a += 1 + 0.5 * (v[i] - 1)
    print(a)


def __starting_point():
    main()


__starting_point()
