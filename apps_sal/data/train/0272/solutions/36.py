class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # box & key & open
        ret = 0
        # status 0:close, 1:open, 2:opened
        # step 1: open boxes, if nothing can be opened, stop
        # step 2: update candies, new boxes, keys(open status)
        # repeat step 1
        n = len(status)
                
        available_to_open = [box for box in initialBoxes if status[box]]
        reachable_boxes = set([box for box in initialBoxes if not status[box]])
        
        while len(available_to_open) > 0:
            box = available_to_open.pop()
            if status[box] == 2:
                continue
                
            ret += candies[box]
            status[box] = 2
            
            for containedBox in containedBoxes[box]:
                reachable_boxes.add(containedBox)
            
            for key in keys[box]:
                if status[key] == 0:
                    status[key] = 1
                
            for containedBox in containedBoxes[box]:
                if status[containedBox] == 1:
                    available_to_open.append(containedBox)
            
            for key in keys[box]:
                if key in reachable_boxes:
                    available_to_open.append(key)
                    
        return ret
                
            

            
        
        
        
        
        
        return ret
