
def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()

    n, k = map(int, input().split())
    s = input()
    n = len(s)
    ans = 0
    for i in range(n - 1):
        if s[i + 1] == s[i]:
            ans += 1
    while ans < n - 1 and k > 0:
        if n - 1 - ans > 1:
            ans += 2
        elif n - 1 - ans == 1:
            ans += 1
        k -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
