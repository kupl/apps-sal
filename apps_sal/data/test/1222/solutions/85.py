def dfs(cnt, num, top):
    if cnt == 10:
        return
    v.add(int(num))
    if top == 0:
        dfs(cnt + 1, '0' + num, top)
        dfs(cnt + 1, '1' + num, top + 1)
    elif top == 9:
        dfs(cnt + 1, '8' + num, top - 1)
        dfs(cnt + 1, '9' + num, top)
    else:
        dfs(cnt + 1, str(top - 1) + num, top - 1)
        dfs(cnt + 1, str(top) + num, top)
        dfs(cnt + 1, str(top + 1) + num, top + 1)


k = int(input())
v = set()
for i in range(10):
    dfs(0, str(i), i)
v = list(v)
v.sort()
v.pop(0)
print(v[k - 1])
