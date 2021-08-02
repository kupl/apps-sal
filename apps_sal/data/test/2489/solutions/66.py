def abc170d_not_divisible():
    n = int(input())
    cnt = 0
    a = sorted(list(map(int, input().split())))
    flgs = [True] * (a[-1] + 1)
    if n == 1:
        print(1)
        return
    for i in range(n):
        if i != n - 1 and a[i] == a[i + 1]:
            flgs[a[i]] = False
            continue
        for j in range(a[i] * 2, a[-1] + 1, a[i]):
            flgs[j] = False
        if flgs[a[i]]:
            cnt += 1
    print(cnt)


abc170d_not_divisible()
