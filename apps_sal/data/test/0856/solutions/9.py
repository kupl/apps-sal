for _ in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    if k > 5:
        if k % 2 == 0:
            k = 4
        else:
            k = 5

    def f(v):
        m = max(v)
        for i in range(n):
            v[i] = m - v[i]
        return v
    for _ in range(k):
        a = f(a)
    print(*a)
