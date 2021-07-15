import queue
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        color_bounds = {}
        for i, row in enumerate(targetGrid):
            for j, color in enumerate(row):
                if not color in color_bounds:
                    color_bounds[color] = {'row': [1e6,-1e6], 'col': [1e6,-1e6]}
                color_bounds[color]['row'][0] = min(color_bounds[color]['row'][0], i)
                color_bounds[color]['row'][1] = max(color_bounds[color]['row'][1], i)
                color_bounds[color]['col'][0] = min(color_bounds[color]['col'][0], j)
                color_bounds[color]['col'][1] = max(color_bounds[color]['col'][1], j)
        graph = collections.defaultdict(list)
        degree = Counter()
        for color, bounds in list(color_bounds.items()):
            seen = set()
            for i in range(bounds['row'][0], bounds['row'][1] + 1):
                for j in range(bounds['col'][0], bounds['col'][1] + 1):
                    other_color = targetGrid[i][j]
                    if other_color != color and other_color not in seen:
                        seen.add(other_color)
                        graph[other_color].append(color)
                        degree[color] += 1
        q = queue.Queue()
        for color in list(color_bounds.keys()):
            if degree[color] == 0:
                q.put(color)
        processed_nodes = 0
        while not q.empty():
            color = q.get()
            processed_nodes += 1
            for next_color in graph[color]:
                degree[next_color] -= 1
                if degree[next_color] == 0:
                    q.put(next_color)
        return processed_nodes == len(color_bounds)
            

