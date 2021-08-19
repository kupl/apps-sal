USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def Cnk(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
        ans //= i + 1
    return ans


def main():
    num = [[0] * 4 for _ in range(19)]
    for i in range(19):
        for j in range(4):
            if j:
                num[i][j] += num[i][j - 1]
            if i >= j:
                num[i][j] += 9 ** j * Cnk(i, j)

    def count(n):
        if n == 0:
            return 0
        n = list(map(int, str(n)))
        l = len(n)
        ans = 0
        for i in range(1, l):
            ans += 9 * num[i - 1][2]
        cur = 3
        for i in range(l):
            if n[i] > 0:
                ans += (n[i] - 1) * num[l - i - 1][cur - 1]
                if i:
                    ans += num[l - i - 1][cur]
                cur -= 1
                if cur <= 0:
                    break
        ans += 1
        return ans
    (q,) = list(map(int, input().split(' ')))
    for _ in range(q):
        (L, R) = list(map(int, input().split(' ')))
        ans = count(R) - count(L - 1)
        print(ans)


def __starting_point():
    main()


__starting_point()
