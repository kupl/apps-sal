def main():
    L = int(input())
    n = 1
    while 2**n <= L:
        n += 1
    n -= 1
    ans = []
    for i in range(1, n + 1):
        ans.append([i, i + 1, 0])
        ans.append([i, i + 1, 2**(i - 1)])
    for i in reversed(range(1, n + 1)):
        if L - 2**(i - 1) >= 2**n:
            ans.append([i, n + 1, L - 2**(i - 1)])
            L -= 2**(i - 1)
    print(n + 1, len(ans))
    for u, v, w in ans:
        print(u, v, w)


def __starting_point():
    main()


__starting_point()
