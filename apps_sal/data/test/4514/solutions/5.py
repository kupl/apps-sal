(n, q) = map(int, input().split())
children = [[] for i in range(n)]
size = [0] * n
for (i, p) in enumerate(map(int, input().split()), 1):
    children[p - 1].append(i)
size = [1] * n
dfs = []
index_to_rank = [0] * n


def traverse():
    visited = [False] * n
    stack = [(0, None)]
    while stack:
        (i, parent) = stack[-1]
        if visited[i]:
            stack.pop()
            if parent is not None:
                size[parent] += size[i]
        else:
            visited[i] = True
            index_to_rank[i] = len(dfs)
            dfs.append(i)
            for j in reversed(children[i]):
                stack.append((j, i))


answer = []


def answer_queries():
    print = answer.append
    for i in range(q):
        (u, k) = map(int, input().split())
        index = u - 1
        if size[index] < k:
            print(-1)
        else:
            print(dfs[index_to_rank[index] + k - 1] + 1)


traverse()
answer_queries()
print('\n'.join(map(str, answer)))
