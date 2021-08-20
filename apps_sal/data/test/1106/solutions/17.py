class Route:

    def __init__(self):
        self.lamps_count = 0
        self.nodes = {}


def solve(n, lamps):
    routes_count = 2 ** n
    max_node_num = 2 ** (n + 1) - 1
    routes = [Route() for _ in range(routes_count)]

    def dfs_pre(node, count=0):
        if node >= routes_count:
            route = routes[node - routes_count]
            route.lamps_count = count
            while node != 0:
                route.nodes[node] = node
                node //= 2
        else:
            dfs_pre(node * 2, count + lamps[(node - 1) * 2])
            dfs_pre(node * 2 + 1, count + lamps[(node - 1) * 2 + 1])

    def dfs_post(node):
        if node > max_node_num:
            return 0
        diffs = []
        for r in routes:
            if node in r.nodes:
                diffs.append(max_lamps_count - r.lamps_count)
        diffs.sort()
        if diffs and diffs[0]:
            for r in routes:
                if node in r.nodes:
                    r.lamps_count += diffs[0]
        return diffs[0] + dfs_post(node * 2) + dfs_post(node * 2 + 1)
    dfs_pre(1)
    max_lamps_count = sorted(routes, key=lambda r: -r.lamps_count)[0].lamps_count
    res = dfs_post(1)
    return res


def main():
    n = int(input().strip())
    lamps = list(map(int, input().strip().split()))
    print(solve(n, lamps))


main()
