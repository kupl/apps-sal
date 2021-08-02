def resolve():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    l = a[0] + k - a[-1]
    for i in range(1, n):
        l = max(l, a[i] - a[i - 1])
    print(k - l)


resolve()
