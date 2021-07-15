from collections import deque

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        grids = targetGrid
        num_to_range = dict()
        for i, row in enumerate(targetGrid):
            for j, val in enumerate(row):
                if val not in num_to_range:
                    # up, down, left, right
                    num_to_range[val] = [i, i, j, j]
                num_to_range[val][0] = min(num_to_range[val][0], i)
                num_to_range[val][1] = max(num_to_range[val][1], i)
                num_to_range[val][2] = min(num_to_range[val][2], j)
                num_to_range[val][3] = max(num_to_range[val][3], j)
        #print(num_to_range)
        
        m = len(grids)
        n = len(grids[0])
        grid_list = [[list() for j in range(n)] for i in range(m)]
        for num, val in list(num_to_range.items()):
            for i in range(val[0], val[1]+1):
                for j in range(val[2], val[3]+1):
                    grid_list[i][j].append(num)

        paths = {val: set() for val in list(num_to_range)}
        for i, row in enumerate(targetGrid):
            for j, val in enumerate(row):
                for parent in grid_list[i][j]:
                    if parent != val:
                        paths[parent].add(val)
                    
        parent_counter = {val: 0 for val in list(num_to_range)}
        for parent, childs in list(paths.items()):
            for child in childs:
                parent_counter[child] += 1
        
        queue = deque()
        for child, cnt in list(parent_counter.items()):
            if cnt == 0:
                queue.append(child)
        
        seen = set()
        while queue:
            parent = queue.popleft()
            seen.add(parent)
            for child in paths[parent]:
                parent_counter[child] -= 1
                if parent_counter[child] == 0:
                    queue.append(child)
                
        
        
        return len(seen) == len(num_to_range)
                

