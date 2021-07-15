class Edge:

    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


def bellman_ford(N, edges, start, goal):
    # Weight Maximization
    MIN_INF = - 10**15
    d = [MIN_INF for _ in range(N)]
    d[start] = 0
    for loop in range(N):
        updated = False
        goal_updated = False
        for edge in edges:
            new_d = edge.weight + d[edge.from_node]
            if d[edge.to_node] < new_d:
                d[edge.to_node] = new_d
                updated = True
                if edge.to_node == goal:
                    goal_updated = True
        if not updated:
            return d[goal]
        if loop == N - 1:
            if not goal_updated:
                return d[goal]
            # exists a positive loop which connected to the goal node.
            return None


def main():
    N, M = list(map(int, input().split(' ')))
    edges = list()
    for _ in range(M):
        a, b, c = list(map(int, input().split(' ')))
        from_node = a - 1 
        to_node = b - 1
        weight = c
        edges.append(Edge(from_node, to_node, weight))
    start, goal = 0, N - 1
    result = bellman_ford(N, edges, start, goal)
    if result is None:
        print('inf')
    else:
        print(result)


def __starting_point():
    main()

__starting_point()
