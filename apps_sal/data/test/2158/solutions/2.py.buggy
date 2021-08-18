def dfs(s=0, p=-1):
    nonlocal a
    nonlocal n
    if len(a[s]) == 1 and p != -1:
        return a[s][0][1]
    o = -1
    pp = -1
    for i in range(len(a[s])):
        if a[s][i][0] != p:
            if o == -1:
                o = dfs(a[s][i][0], s)
            else:
                o = max(o, dfs(a[s][i][0], s))
        else:
            pp = i
    if p != -1:
        return o + a[s][pp][1]
    return o


n = int(input())
a = [[] for i in range(n)]
for i in range(n - 1):
    x, y, z = list(map(int, input().split()))
    a[x] += [[y, z]]
    a[y] += [[x, z]]
print(dfs())
