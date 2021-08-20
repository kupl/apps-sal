def main():
    (n, m) = map(int, input().split(' '))
    s = [0] * m
    c = [0] * m
    for i in range(m):
        (s[i], c[i]) = map(int, input().split(' '))
    ans = [-1] * n
    for i in range(m):
        if ans[s[i] - 1] != -1 and ans[s[i] - 1] != c[i]:
            print(-1)
            return
        ans[s[i] - 1] = c[i]
    if ans[0] == 0:
        if n == 1:
            print(0)
            return
        print(-1)
        return
    for i in range(n):
        if ans[i] == -1:
            if i == 0:
                if n == 1:
                    print(0)
                    return
                print(1, end='')
            else:
                print(0, end='')
        else:
            print(ans[i], end='')
    print()


def __starting_point():
    main()


__starting_point()
