
"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""

n = None
p = []
a = []
visited = []
ids = []
values = []


def dfs(u):
    nonlocal visited, ids, values

    visited[u] = True
    for v in range(n):
        if (not visited[v]) and (a[u][v] == '1'):
            ids.append(v)
            values.append(p[v])
            dfs(v)


def main():
    nonlocal n, p, a, visited

    n = int(input())
    p = list((int(_) for _ in input().split()))
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a[i] = input()

    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        nonlocal ids, values
        ids = [i]
        values = [p[i]]
        dfs(i)
        ids = sorted(ids)
        values = sorted(values)
        for x, y in zip(ids, values):
            p[x] = y

    print(" ".join(str(_) for _ in p))


def __starting_point():
    main()


__starting_point()
