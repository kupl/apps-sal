class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        least_infections = len(graph)
        node_to_remove = initial[0]

        for i in initial:

            total_infected = 0

            q = initial[:]
            q.remove(i)
            visited = set()

            while q != []:
                v = q.pop()
                if v != i and not v in visited:
                    total_infected += 1
                    visited.add(v)
                    for j, edge in enumerate(graph[v]):
                        if j != i and (edge == 1) and not (j in visited):
                            q.append(j)

            if total_infected < least_infections:
                least_infections = total_infected
                node_to_remove = i
            elif total_infected == least_infections:
                node_to_remove = min(i, node_to_remove)

        return node_to_remove
