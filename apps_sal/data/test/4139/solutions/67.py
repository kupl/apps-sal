n = int(input())


def dfs(cur, use, cnt):
    if cur > n:
        return
    if use == 7:
        cnt.append(1)
    dfs(cur * 10 + 7, use | 1, cnt)
    dfs(cur * 10 + 5, use | 2, cnt)
    dfs(cur * 10 + 3, use | 4, cnt)


cnt = []
dfs(0, 0, cnt)
print(len(cnt))
