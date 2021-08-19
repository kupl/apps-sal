def dsum(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res


for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    p = 1
    ans = 0
    csum = dsum(n)
    while csum > s:
        add = 10 * p - n % (10 * p)
        if add == 10 * p:
            add = 0
        ans += add
        n += add
        csum = dsum(n)
        p *= 10
    print(ans)
