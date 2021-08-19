def __starting_point():
    s = input().rstrip().split()
    N = int(s[0])
    K = int(s[1])
    a = list(map(int, list(input().rstrip().split())))
    diff = []
    for i in range(1, N):
        diff.append([i, a[i] - a[i - 1]])
    diff = sorted(diff, key=lambda x: -x[1])
    res = max(a) - min(a)
    k = 0
    while k < K - 1 and k < len(diff):
        res -= diff[k][1]
        k += 1
    print(res)


__starting_point()
