from sys import stdin


def solve():
    s = stdin.readline().strip()
    n = len(s)

    sfa = [[0, 0] for i in range(n + 1)]
    sfb = [[0, 0] for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        sfa[i][:] = sfa[i + 1][:]
        sfb[i][:] = sfb[i + 1][:]
        if s[i] == 'a':
            sfa[i][i % 2] += 1
        else:
            sfb[i][i % 2] += 1

    ans = [0, 0]
    for i in range(n):
        if s[i] == 'a':
            ans[0] += sfa[i + 1][i % 2]
            ans[1] += sfa[i + 1][(i + 1) % 2]
        else:
            ans[0] += sfb[i + 1][i % 2]
            ans[1] += sfb[i + 1][(i + 1) % 2]

    print(ans[1], ans[0] + n)


solve()
