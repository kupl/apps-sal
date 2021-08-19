def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a>>>>>
    # b<<<<<
    def f(m):
        ans = 0
        for i in a:
            ans += max(0, m - i)
        for i in b:
            ans += max(0, i - m)
        return ans
    l = 0
    r = 10**9 + 3

    while r - l > 2:
        m1 = l + (r - l) // 3
        m2 = m1 + (r - l) // 3
        if f(m1) >= f(m2):
            l = m1
        else:
            r = m2

    print(min(f(l), f(l + 1), f(r)))


main()
