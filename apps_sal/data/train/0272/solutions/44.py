class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
    
        bfs = [x for x in initialBoxes if status[x]]
        
        for i in bfs:
            for j in containedBoxes[i]:
                boxes.add(j)
                if status[j]:
                    bfs.append(j)
                                    
            for k in keys[i]:
                if status[k] == 0 and k in boxes:
                    bfs.append(k)
                status[k] = 1
                    
        return sum([candies[i] for i in boxes if status[i]]) 
