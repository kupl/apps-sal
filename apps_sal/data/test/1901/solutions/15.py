from collections import defaultdict
merge_matrix = defaultdict(list)
n, m = list(map(int, input().split()))
price_list = [int(x) for x in input().split()]
summary = 0
visited = set()


def dfs(edge):
    queue = []
    visited.add(edge)
    queue.append(edge)
    lowest_cost = price_list[edge-1]
    while len(queue) > 0:
        cur_edge = queue.pop()
        for i in merge_matrix[cur_edge]:
            if i not in visited:
                lowest_cost = min(lowest_cost, price_list[i - 1])
                queue.append(i)
                visited.add(i)
    return lowest_cost


for i in range(m):
    x, y = list(map(int, input().split()))
    merge_matrix[x].append(y)
    merge_matrix[y].append(x)
for i in range(1, n+1):
    if i not in visited:
        summary += dfs(i)
for i in range(1, n+1):
    if i not in visited:
        summary += price_list[i-1]
print(summary)

