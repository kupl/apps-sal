def solve():
    n, a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x.append(a)
    x.sort()
    bi = 0
    for i in range(n + 1):
        if x[i] == a:
            bi = i
            break
    ans = float('inf')
    for s in range(2):
        l = 0
        r = 0
        ok = x[s] == a
        for i in range(s + 1, s + n):
            ok = ok or x[i] == a
            if i <= bi:
                l += x[i] - x[i - 1]
            else:
                r += x[i] - x[i - 1]
        if ok:
            ans = min(ans, min(l, r) * 2 + max(l, r))
    print(ans)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
