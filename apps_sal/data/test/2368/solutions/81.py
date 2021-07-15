# Values

# 各連結成分においてa_iの総和とb_iの総和が等しければよい

from collections import deque

N, M = list(map(int, input().split()))
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
graph = [[] for i in range(N)]
for i in range(M):
    c, d = list(map(int, input().split()))
    graph[c - 1].append(d - 1)
    graph[d - 1].append(c - 1)
graph = tuple(tuple(l) for l in graph)

unreached = set(range(N))
queue = deque()
judge = "Yes"
while len(unreached) > 0:
    node = unreached.pop()
    queue.append(node)
    sum_a = a[node]
    sum_b = b[node]

    # 頂点を幅優先探索
    while len(queue) > 0:
        for node in graph[queue.pop()]:
            if node in unreached:
                unreached.remove(node)
                queue.append(node)
                sum_a += a[node]
                sum_b += b[node]
    
    if sum_a != sum_b:
        judge = "No"
        break

print(judge)

