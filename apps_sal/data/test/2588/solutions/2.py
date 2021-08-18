def mp():
    return map(int, input().split())


def f(i, j):
    return a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1] == 1


q = int(input())

for qq in range(q):
    n, a, b = mp()
    s = input()
    dp_u = [0] * (n + 1)
    dp_d = [0] * (n + 1)
    dp_u[0] = 10 ** 20
    dp_d[0] = b

    for i in range(1, n):
        dp_u[i] = min(dp_u[i - 1] + a, dp_d[i - 1] + 2 * a) + 2 * b
        if s[i] == '0' and s[i - 1] == '0':
            dp_d[i] = min(dp_u[i - 1] + 2 * a, dp_d[i - 1] + a) + b
        else:
            dp_d[i] = 10 ** 20

    print(min(dp_d[n - 1] + a, dp_u[n - 1] + 2 * a) + b)
