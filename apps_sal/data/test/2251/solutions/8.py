from collections import defaultdict


def main():
    n, m = list(map(int, input().split()))
    edges = defaultdict(lambda: defaultdict(list))
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        d = edges[c]
        d[a].append(b)
        d[b].append(a)

    def dfs(t):
        chain.add(t)
        dd = color.get(t, ())
        for y in dd:
            if y not in chain:
                dfs(y)

    res = []
    chain = set()
    for _ in range(int(input())):
        a, b = list(map(int, input().split()))
        x = 0
        for color in list(edges.values()):
            chain.clear()
            dfs(a)
            if b in chain:
                x += 1
        res.append(str(x))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
