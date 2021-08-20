s = input()
n = len(s)


def dfs(i, tmp):
    if i == n - 1:
        return sum(list(map(int, tmp.split('+'))))
    return dfs(i + 1, tmp + s[i + 1]) + dfs(i + 1, tmp + '+' + s[i + 1])


print(dfs(0, s[0]))
