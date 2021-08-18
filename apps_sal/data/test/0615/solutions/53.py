def main():
    from bisect import bisect_left

    n = int(input())
    a = list(map(int, input().split()))

    cs = [0] * n
    for i in range(n):
        cs[i] = cs[i - 1] + a[i]

    ans = 10**15
    for middle in range(2, n - 1):
        first = bisect_left(cs, cs[middle - 1] // 2, lo=1, hi=middle)
        if abs((cs[middle - 1] - cs[first - 1]) - cs[first - 1]) < abs((cs[middle - 1] - cs[first]) - cs[first]):
            p = cs[first - 1]
            q = cs[middle - 1] - cs[first - 1]
        else:
            p = cs[first]
            q = cs[middle - 1] - cs[first]

        last = bisect_left(cs, (cs[-1] + cs[middle - 1]) // 2, lo=middle + 1, hi=n)
        if abs((cs[-1] - cs[last - 1]) - (cs[last - 1] - cs[middle - 1])) < abs((cs[-1] - cs[last]) - (cs[last] - cs[middle - 1])):
            r = cs[last - 1] - cs[middle - 1]
            s = cs[-1] - cs[last - 1]
        else:
            r = cs[last] - cs[middle - 1]
            s = cs[-1] - cs[last]

        diff = max(p, q, r, s) - min(p, q, r, s)
        if diff < ans:
            ans = diff

    print(ans)


main()
