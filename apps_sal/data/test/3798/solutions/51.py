def solve():
    n = int(input())
    s = int(input())
    if n == s:
        print((n + 1))
        return
    ret = float("inf")
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        tmp = 0
        tn = n
        while tn:
            tmp += tn % i
            tn //= i
        if tmp == s:
            ret = i
            break

    if ret == float("inf") and n > s:
        t = n - s
        sqrt1 = int(t ** 0.5)
        for i in range(1, min(s, sqrt1) + 1):
            if t % i == 0 and s - i <= t // i and t // i + 1 > sqrt:
                ret = min(ret, t // i + 1)
    print((ret if ret != float("inf") else -1))


solve()
