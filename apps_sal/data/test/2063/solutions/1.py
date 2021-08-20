def main():

    def check(x):
        b = [0] * (n + 1)
        curr = 0
        day = 0
        for i in range(n):
            curr += b[i]
            if a[i] + curr < x:
                tmp = x - a[i] - curr
                b[min(i + w, n)] -= tmp
                day += tmp
                curr += tmp
            if day > m:
                break
        return day
    (n, m, w) = map(int, input().split())
    a = list(map(int, input().split()))
    l = min(a)
    r = max(a) + m + 1
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid) <= m:
            l = mid
        else:
            r = mid
    print(l)


main()
