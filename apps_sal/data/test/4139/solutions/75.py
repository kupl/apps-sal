N = int(input())


def dfs(current, judge, count):
    if current > N:
        return
    if judge == 7:
        count.append(1)
    dfs(current * 10 + 7, judge | 4, count)
    dfs(current * 10 + 5, judge | 2, count)
    dfs(current * 10 + 3, judge | 1, count)


cnt = []
dfs(0, 0, cnt)
print(sum(cnt))
