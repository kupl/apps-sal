def main():
    n = int(input())
    N = 2 * n
    ans = [None] * N
    a = [list(map(int, input().split())) for i in range(N - 1)]

    used = [False] * N
    for i in range(n):
        Max = -(10 ** 9)
        for i in range(N - 1):
            if used[i + 1]:
                continue
            for j in range(i + 1):
                if not used[j] and a[i][j] > Max:
                    Max = a[i][j]
                    x, y = i + 1, j
        used[x] = used[y] = True
        ans[x], ans[y] = y + 1, x + 1

    print(' '.join(map(str, ans)))


main()
