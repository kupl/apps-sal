def dfs(i, sum1):
    nonlocal ss
    # print(i,sum1)
    if i == len(s):
        return sum(list(map(int, sum1.split("+"))))
    return dfs(i + 1, sum1 + s[i]) + dfs(i + 1, sum1 + "+" + s[i])


s = input()
ss = 0
print(dfs(1, s[0]))
