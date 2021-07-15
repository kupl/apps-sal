def dfs(i, f):
    if i == n - 1:
        return sum(list(map(int, f.split('+'))))

    return dfs(i + 1, f + a[i + 1]) + dfs(i + 1, f + '+' + a[i + 1])


a = input()
n = len(a)

print((dfs(0, a[0])))

