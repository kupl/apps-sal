n, m, k = list(map(int, input().split()))

t = [0] + list(map(int, input().split()))

if m == 1:

    t.sort()

    print(sum(t[- k:]))

else:

    for i in range(n):
        t[i + 1] += t[i]

    t = [t[j + m] - t[j] for j in range(n - m + 1)]

    u, v = [0] * (n - m + 1), [0] * (n - m + 1)

    k *= m

    n += 1 - k

    for j in range(n):
        u[j] = max(t[j], u[j - 1])

    for i in range(m, k, m):

        for j in range(i, n + i):
            v[j] = max(u[j - m] + t[j], v[j - 1])

        u, v = v, u

    print(u[-1])
