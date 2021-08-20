def dfs(u):
    if used[u]:
        return False
    used[u] = 1
    for i in range(m):
        if abs(a[u] - b[i]) < 2 and (pair[i] == -1 or dfs(pair[i])):
            pair[i] = u
            return True
    return False


(n, a, m, b) = (int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split())))
pair = [-1] * m
for i in range(n):
    used = [0] * n
    dfs(i)
print(sum((1 for p in pair if p != -1)))
