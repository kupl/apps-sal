N = int(input())

def dfs(n):
    if int(n) > N:
        return 0
    res = 0
    if all(n.count(c) for c in "753"):
        res = 1
    for c in "753":
        res += dfs(n+c)
    return res

print(dfs('0'))
