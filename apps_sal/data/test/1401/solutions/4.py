"""
	Author		: Arif Ahmad
	Date  		: 18-06-16
	Algo  		: DFS
	Difficulty	: Medium
"""


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    g = [[] for x in range(n + 1)]
    cost = {}
    for i in range(2, n + 1):
        (p, c) = list(map(int, input().split()))
        g[p].append((i, c))
    stack = [(1, 0, False)]
    ans = 0
    while stack:
        (u, dist, sad) = stack.pop()
        sad = sad or dist > a[u]
        if sad:
            ans += 1
        for (v, c) in g[u]:
            stack.append((v, max(0, dist + c), sad))
    print(ans)


def __starting_point():
    main()


__starting_point()
