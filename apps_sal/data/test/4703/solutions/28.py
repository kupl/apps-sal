s = input()
n = len(s)


def dfs(now, total, i):
    if i == n:
        return total + now
    else:
        res = 0
        res += dfs(now * 10 + int(s[i]), total, i + 1)
        res += dfs(int(s[i]), total + now, i + 1)
        return res


print((dfs(int(s[0]), 0, 1)))
