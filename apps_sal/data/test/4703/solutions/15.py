s = input()
l = len(s)


def dfs(i, x):
    if i == l - 1:
        return eval(x)
    rep0 = dfs(i + 1, x + s[i + 1])
    rep1 = dfs(i + 1, x + "+" + s[i + 1])
    return rep0 + rep1


ans = dfs(0, s[0])
print(ans)

