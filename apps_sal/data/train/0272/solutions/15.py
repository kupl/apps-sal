

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        found = [0] * len(status)
        hasKeys = status
        queue = collections.deque()
        
        for box in initialBoxes:
            found[box] = 1
            if hasKeys[box]:
                queue.append(box)
        
        res = 0
        while queue:
            box = queue.popleft()
            res += candies[box]
            for t in containedBoxes[box]:
                found[t] = 1
                if hasKeys[t]:
                    queue.append(t)
            
            for t in keys[box]:
                if not hasKeys[t] and found[t]:
                    queue.append(t)
                hasKeys[t] = 1
        
        return res
        
        
        
        
        
        

