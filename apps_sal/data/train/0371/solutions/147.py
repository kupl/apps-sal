class Solution:
    def numBusesToDestination(self, routes, S, T):
        to_lines = collections.defaultdict(set)  # key: step; value: line pass this stop
        for i, line in enumerate(routes):
            for j in line:
                to_lines[j].add(i)

        queue = [S]
        visited = {S}
        step = 0
        while queue:
            new_queue = []
            for stop in queue:
                if stop == T: 
                    return step
                for i in to_lines[stop]:
                    for j in routes[i]:
                        if j not in visited:
                            new_queue.append(j)
                            visited.add(j)
                    
                    #routes[i] = []  # seen route
            queue = new_queue
            step += 1
        return -1
