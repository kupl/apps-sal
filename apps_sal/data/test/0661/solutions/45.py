import sys
MOD = 10 ** 9 + 7
INF = 10 ** 10
sys.setrecursionlimit(100000000)
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def main():
    (m, k) = map(int, input().split())
    if k >= pow(2, m):
        print(-1)
        return
    if m == 1:
        if k == 1:
            print(-1)
        else:
            print('{0} {0} {1} {1}'.format(0, 1))
        return
    ans = [k]
    ans2 = [k]
    lim = pow(2, m)
    for i in range(lim):
        if i != k:
            ans.append(i)
        if lim - i - 1 != k:
            ans2.append(lim - i - 1)
    ans += ans2
    print(*ans)


def __starting_point():
    main()


__starting_point()
