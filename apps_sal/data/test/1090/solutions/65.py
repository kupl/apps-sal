def main():
    n, k = list(map(int, input().split()))
    s = input()
    hp = [0] * n
    for i in range(n):
        if i > 0:
            if s[i] == s[i - 1] == 'L':
                hp[i] = 1
        if i < n - 1:
            if s[i] == s[i + 1] == 'R':
                hp[i] = 1
    ans = sum(hp)
    ans = min(ans + 2 * k, n - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
