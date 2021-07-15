class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        
        # topo sort
        parent = collections.defaultdict(int)
        for i,row in enumerate(containedBoxes):
            for j in row:
                parent[j] = i
        
        n = len(status)
        bfs = collections.deque([(i,False) for i in initialBoxes])
        res = 0
        seen = set()
        while bfs:
            #print(bfs)
            box,st = bfs.popleft()
            if box in seen:
                continue
            if status[box]==0:
                if st:
                    return res
                bfs.append((box,True))
                continue
            seen.add(box)
            res+=candies[box]
            for key in keys[box]:
                status[key] = 1
            for cbox in containedBoxes[box]:
                bfs.append((cbox,False))
            
            
            
        return res
