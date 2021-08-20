S1 = input()
S2 = input()
L = len(S1)
memo = {}


def dfs(i, p1, p2):
    if i == L:
        return 0
    key = (i, p1, p2)
    if key in memo:
        return memo[key]
    r = 0
    if S1[i] == S2[i] == '0':
        if p1 > 0 or p2 > 0:
            if p1 > 0 < p2:
                r = max(dfs(i + 1, 1, 0), dfs(i + 1, 0, 1)) + 1
            else:
                r = dfs(i + 1, 0, 0) + 1
        else:
            r = dfs(i + 1, 1, 1)
    elif S1[i] == '0':
        if p1 > 0 and p2 > 0:
            r = dfs(i + 1, 0, 0) + 1
        else:
            r = dfs(i + 1, 1, 0)
    elif S2[i] == '0':
        if p1 > 0 and p2 > 0:
            r = dfs(i + 1, 0, 0) + 1
        else:
            r = dfs(i + 1, 0, 1)
    else:
        r = dfs(i + 1, 0, 0)
    memo[key] = r
    return r


print(dfs(0, 0, 0))
