import collections
n = int(input())


def bfs(stack1):
    while True:
        stack2 = list()
        while stack1:
            vertex = stack1.pop()
            if not visited1[vertex]:
                visited1[vertex] = 1
                for v in inp[vertex]:
                    if not visited2[v]:
                        stack2.append(v)
        if not stack2:
            return
        stack1 = list()
        while stack2:
            vertex = stack2.pop()
            if not visited2[vertex]:
                visited2[vertex] = 1
                for v in inp[vertex]:
                    if not visited1[v]:
                        stack1.append(v)

        if not stack1:
            return


inp = collections.defaultdict(list)
for _ in range(n - 1):
    v1, v2 = list(map(int, input().split()))
    inp[v1].append(v2)
    inp[v2].append(v1)
visited1, visited2 = [0] + [0] * n, [0] + [0] * n
bfs([1])
print(sum(visited1) * sum(visited2) - (n - 1))

"""
6
2 1
3 1
4 1
5 2
2 6
"""
