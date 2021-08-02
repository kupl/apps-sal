def dfs(i, a, b):
    nonlocal ans
    if i == 3:
        if a == b:
            ans = 1
    else:
        dfs(i + 1, a + t[i], b)
        dfs(i + 1, a, b + t[i])


t = list(map(int, input().split()))
ans = 0
dfs(-1, 0, 0)
if ans == 1:
    print("Yes")
else:
    print("No")
