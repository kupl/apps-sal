class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # open_box: 有key有box
        # close_box: 有box没key
        # key_set: 有key没box
        # visited
        open_box = []
        close_box = set()
        key_set = set([i for i in range(len(status)) if status[i]==1])
        visited = [False for _ in range(len(status))]
        count = 0
        for box in initialBoxes:
            if status[box]==1:
                open_box.append(box)
            else:
                close_box.add(box)        
        while open_box:
            box = open_box.pop()
            visited[box] = True
            count += candies[box]
            for key in keys[box]:
                if visited[key]:
                    continue
                if key in close_box:
                    open_box.append(key)
                    close_box.remove(key)
                else:
                    key_set.add(key)
            for c_box in containedBoxes[box]:
                if visited[c_box]:
                    continue
                elif c_box in key_set:
                    open_box.append(c_box)
                else:
                    close_box.add(c_box)
            for key in key_set:
                if key in close_box:
                    open_box.append(key)
                    close_box.remove(key)
        return count
            
                    
                
            

