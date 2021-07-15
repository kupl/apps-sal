N = int(input())


def dfs(current, judge, count):
    if current > N:
        return
    if judge == 0b111:
        count.append(1)

    dfs(current * 10 + 7, judge | 0b100, count)
    dfs(current * 10 + 5, judge | 0b010, count)
    dfs(current * 10 + 3, judge | 0b001, count)


cnt = []
dfs(0, 0, cnt)
print(sum(cnt))
