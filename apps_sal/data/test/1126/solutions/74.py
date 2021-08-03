def main():
    n, x, m = list(map(int, input().split()))
    s = set()
    L = []
    ans = 0
    while n > 0:
        s.add(x)
        L.append(x)
        ans += x
        x = x * x % m
        n -= 1
        if x in s:
            break
    else:
        print(ans)
        return
    L = L[L.index(x):]
    q, r = divmod(n, len(L))
    ans += sum(L) * q
    ans += sum(L[:r])
    print(ans)


def __starting_point():
    main()


__starting_point()
