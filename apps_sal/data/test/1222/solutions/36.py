def dfs(d: int, v: int, all: list):
    if d == 11:
        return
    all.append(v)
    if list(str(v))[-1] == "0":
        dfs(d + 1, 10 * v + int(list(str(v))[-1]) + 1, all)
        dfs(d + 1, 10 * v + int(list(str(v))[-1]), all)
    elif list(str(v))[-1] == "9":
        dfs(d + 1, 10 * v + int(list(str(v))[-1]) - 1, all)
        dfs(d + 1, 10 * v + int(list(str(v))[-1]), all)
    else:
        dfs(d + 1, 10 * v + int(list(str(v))[-1]) + 1, all)
        dfs(d + 1, 10 * v + int(list(str(v))[-1]), all)
        dfs(d + 1, 10 * v + int(list(str(v))[-1]) - 1, all)


k = int(input())
all = []
for i in range(1, 10):
    dfs(1, i, all)
all.sort()
print((all[k - 1]))
