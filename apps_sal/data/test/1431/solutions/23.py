def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = set()

    for i in range(n, 0, -1):
        now = 0
        for j in range(2 * i, n + 1, i):
            if j in ans:
                now += 1
        if now % 2 != a[i - 1]:
            ans.add(i)

    return ans


def __starting_point():
    x = solve()
    print(len(x))
    print(*x, sep=' ')


__starting_point()
