def solvea():
    n = int(input())
    d = int(input())
    e = 5 * int(input())
    best = 0
    for enr in range(n // e + 1):
        curr = e * enr
        curr += d * ((n - curr) // d)
        if curr <= n and curr > best:
            best = curr
    print(n - best)


def solveb():
    a = int(input())
    b = int(input())
    n = int(input())
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            if i + j == n:
                ans += 1
    print(ans)


def __starting_point():
    solvea()


__starting_point()
