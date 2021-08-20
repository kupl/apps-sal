t = 1
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    data = [0] * (n + 1)
    for i in range(n):
        data[a[i]] += 1
    S = set(a)
    m = len(S)

    def cond(t):
        (q, r) = (n // (t + 1), n % (t + 1))
        if r > m:
            return False
        check = 0
        for i in range(1, n + 1):
            if data[i] > q + 1:
                return False
            elif data[i] == q + 1:
                check += 1
        return r >= check
    ok = 0
    ng = n
    while ng - ok > 1:
        test = (ng + ok) // 2
        if cond(test):
            ok = test
        else:
            ng = test
    print(ok)
