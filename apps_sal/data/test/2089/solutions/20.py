class Node:
    def __init__(self, label):
        self.label, self.ways, self.distances = label, set(), dict()

    def connect(self, other):
        self.ways.add(other)


class Graph:
    def __init__(self, count):
        self.nodes = [Node(i) for i in range(count)]

    def connect(self, a, b):
        node_a, node_b = self.nodes[a], self.nodes[b]
        node_a.connect(node_b)
        node_b.connect(node_a)

    def fill_distances(self, start):
        looked, queue, next_queue = {start}, {start}, set()
        start.distances[start] = 0
        while len(queue) + len(next_queue) > 0:
            for node in queue:
                for neighbour in node.ways:
                    if neighbour not in looked:
                        looked.add(neighbour)
                        next_queue.add(neighbour)
                        neighbour.distances[start] = node.distances[start] + 1
            queue, next_queue = next_queue, set()


def repeat(elem): 
    while True: 
        yield elem
def readline(types=repeat(int)):
    return [x[0](x[1]) for x in zip(types, input().split())]


def readinput():
    nodes, edges, start, finish = readline()
    start, finish = start - 1, finish - 1
    
    graph = Graph(nodes)
    for i in range(edges):
        a, b = readline()
        a, b = a - 1, b - 1
        graph.connect(a, b)

    return graph, graph.nodes[start], graph.nodes[finish]


def main():
    graph, start, finish = readinput()
    graph.fill_distances(start)
    graph.fill_distances(finish)

    distance = start.distances[finish]
    answer = 0
    for i in range(len(graph.nodes)):
        for j in range(i + 1, len(graph.nodes)):
            node_a, node_b = graph.nodes[i], graph.nodes[j]
            if node_a in node_b.ways: 
                continue
            if node_a.distances[start] + 1 + node_b.distances[finish] < distance:
                continue
            if node_a.distances[finish] + 1 + node_b.distances[start] < distance:
                continue
            answer += 1

    print(answer)


main()


