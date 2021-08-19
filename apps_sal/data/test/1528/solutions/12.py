N, X = list(map(int, input().split()))

burger_size = [1]
patty_num = [1]
for i in range(50):
    burger_size.append(2 * burger_size[-1] + 3)
    patty_num.append(2 * patty_num[-1] + 1)


# レベルnバーガーの下からx段目までに含まれるパティの数を返す
def dfs(n, x):
    if burger_size[n] == x:
        return patty_num[n]

    if x == 1:
        return 0

    elif 1 < x <= 1 + burger_size[n - 1]:
        return dfs(n - 1, x - 1)

    elif x == 1 + burger_size[n - 1] + 1:
        return patty_num[n - 1] + 1

    elif 1 + burger_size[n - 1] + 1 < x < burger_size[n]:
        return patty_num[n - 1] + 1 + dfs(n - 1, x - burger_size[n - 1] - 2)


print((dfs(N, X)))
