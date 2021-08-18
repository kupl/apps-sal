def dfs(i, sall):
    if i == lenS:
        return (sall)
    return dfs(i + 1, sall + "+" + s[i]) + "+" + dfs(i + 1, sall + s[i])


s = input()
lenS = len(s)
print(sum(map(int, dfs(1, s[0]).split("+"))))
