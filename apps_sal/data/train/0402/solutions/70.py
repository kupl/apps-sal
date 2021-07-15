class Solution:
    
    def isEscapePossible(self, blocked, source, target):
        blocked = set(map(tuple, blocked))
        source = tuple(source)
        target = tuple(target)
        
        def neighbors(node):
            i, j = node
            return (
                (i+di, j+dj)
                for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= i+di < 10**6
                if 0 <= j+dj < 10**6
                if (i+di, j+dj) not in blocked
            )
        
        def mhat_dist(node0, node1):
            i0, j0 = node0
            i1, j1 = node1
            return abs(i0-i1) + abs(j0-j1)
        
        stack = [source]
        visited = {source}
        exceeded_threshold = False
        while stack:
            node = stack.pop()
            if node == target:
                return True
            if mhat_dist(source, node) > 200:
                exceeded_threshold = True
                break
            new_nodes = set(neighbors(node)) - visited
            visited.update(new_nodes)
            stack.extend(new_nodes)
            
        if not exceeded_threshold:
            return False
        
        stack = [target]
        visited = {target}
        while stack:
            node = stack.pop()
            if mhat_dist(source, node) > 200:
                return True
            new_nodes = set(neighbors(node)) - visited
            visited.update(new_nodes)
            stack.extend(new_nodes)
        return False
        
                

