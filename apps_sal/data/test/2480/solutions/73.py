def main():
    (n, k) = map(int, input().split())
    b = list(map(int, input().split()))
    a = [0] * (n + 1)
    for i in range(n):
        a[i + 1] = b[i]
    for i in range(n + 1):
        if 0 < i:
            a[i] += a[i - 1]
        a[i] %= k
    for i in range(1, n + 1):
        a[i] = (a[i] - i % k + k) % k
    dic = {}
    ans = 0
    (l, r) = (0, 0)
    while r < n + 1:
        x = a[r]
        if k <= r - l:
            dic[a[l]] -= 1
            l += 1
        if x in dic.keys():
            ans += dic[x]
            dic[x] += 1
        else:
            dic[x] = 1
        r += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
