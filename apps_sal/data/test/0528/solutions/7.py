def read():
    n, m = list(map(int, input().rstrip().split()))
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        a, b = list(map(int, input().rstrip().split()))
        graph[a].add(b)
        graph[b].add(a)
        graph[a].add(a)
        graph[b].add(b)
    return (graph, n)

def main():
    graph, n = read()
    seen = set()
    for i in range(1, n + 1):
        if len(graph[i]) > 0 and i not in seen:
            if not all(graph[i] == graph[j] for j in graph[i]):
                return False
            seen |= graph[i]
    return True

def __starting_point():
    if main():
        print('YES')
    else:
        print('NO')

__starting_point()
