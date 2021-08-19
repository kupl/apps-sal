def solve():
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for i in range(1, len(a)):
        s = a[i] + a[i - 1]
        moar = 0
        if s < k:
            moar = k - s
        a[i] += moar
        res += moar
    print(res)
    print(' '.join(map(str, a)))


solve()
