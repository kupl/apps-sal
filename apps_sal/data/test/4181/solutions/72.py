def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = [0] * (n + 1)
    f[0] += min(a[0], b[0])
    f[1] += min(a[1], b[0] - f[0])
    a[1] -= f[1]
    for i in range(1, n):
        f[i] += min(a[i], b[i])
        f[i + 1] += min(a[i + 1], b[i] - min(a[i], b[i]))
        a[i + 1] -= f[i + 1]
    print(sum(f))


resolve()
